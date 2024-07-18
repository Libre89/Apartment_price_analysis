import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from itertools import product
import numpy as np

# load city population of CZ
def get_city_population(cities):
    '''Create dictionary {city: population}'''
    csv_file_path = 'city_population.csv'
    df = pd.read_csv(csv_file_path, delimiter=';')
    df['population'] = df['population'].str.replace('\xa0', '')
    df.sort_values('population')
    #city_population = dict(zip(df['city'], df['population']))
    city_population = dict(zip(df['city'], df['population']))
    population = {city : int(city_population[city]) for city in cities}
    return population

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'cs,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
}

with requests.session() as s:
    city_all = ['Praha', 'Brno', 'Ostrava', 'Olomouc']
    flat_type_all = ['1+kk', '2+kk', '3+kk']
    population = get_city_population(city_all)
    page = 1
    end_page = []
    url = ''
    url_list = []
    df_list = []    

    flat_type_city_combinations = list(product(city_all, flat_type_all))
    print(flat_type_city_combinations)

    for city, flat_type in flat_type_city_combinations:
        url_list = []
        url_first_page = 'https://reality.idnes.cz/s/prodej/byty/' + flat_type + '/' + city

        # OPRAVA
        request = s.get(url_first_page, headers=headers)
        soup_btn = BeautifulSoup(request.content, 'html.parser')
        btn_element = soup_btn.find_all('a', class_='btn btn--border paging__item')
        print(f'Working on {city} disposition {flat_type}.')

        if btn_element:
            elements_str = ''.join(str(btn_element[-1]))
            elements_str = re.findall(r'page=(\d+)', elements_str)

            end_page = int(elements_str[0])

            url_list = ['https://reality.idnes.cz/s/prodej/byty/' + flat_type + '/' + city + ('/?page=' + str(page) if page > 0 else '') for page in range(end_page + 1)]
        


        url_list.append(url_first_page)
        
        request_list = [(s.get(url, headers=headers)) for url in url_list]

        soup = ''
        soup_list = []

        soup_list = [BeautifulSoup(request.content, 'html.parser') for request in request_list]

        for soup in soup_list:
            price_elements = soup.find_all('p', class_='c-products__price')
            address_elements = soup.find_all('p', class_='c-products__info')
            square_meters_elements =  soup.find_all('h2', class_='c-products__title')

            for price, address, square_meters in zip(price_elements, address_elements, square_meters_elements):
                price_text = price.text.strip() 
                address_text = address.text.strip()
                square_meters = square_meters.text.strip()
                df_list.append({'price': price_text, 'address':address_text, 'square_meters': square_meters, 'flat_type': flat_type, 'city': city})

    df = pd.DataFrame(df_list) 

    df['price'] = df['price'].str.extract(r'(\d+\s?\d*\s?\d*)')
    df['price'] = df['price'].replace("\s+", '', regex=True)
    df['price'] = df['price'].astype(float)

    df['square_meters'] = df['square_meters'].str.extract(r'(\d+\sm²$)')
    df['square_meters'] = df['square_meters'].replace("m²", '', regex=True)
    df['square_meters'] = df['square_meters'].astype(float)

    #df_no_NAN = df.copy()
    #df_no_NAN.dropna(subset=['price'], ignore_index=True)

    df['price_per_sq_meter'] = df['price'] / df['square_meters']
    df['price_per_sq_meter'] = df['price_per_sq_meter'].astype(float).round(2)
    

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i]+2,y[i], ha = 'center')


# OVERVIEW BAR PLOT
def overview_bar_plot():  
    # Data
    categories  = ['All advertised apartments', 'Apartments advertised with price', 'Apartments advertised without price']
    
    total_num_data = df.shape[0]
    incorrect__num_data = df['price'].isna().sum()
    correct_num_data = total_num_data - incorrect__num_data
    count = [total_num_data, correct_num_data, incorrect__num_data]

    # Create bar plot
    plt.figure(figsize=(11, 6))
    plt.bar(categories , count, color=['#227ad0', '#009146', '#c34a54'])

    # Titles and labels
    plt.title("Overview of advertised apartments", fontsize = 16)
    #plt.xlabel("Advertised types", fontsize = 12, labelpad = 5)
    plt.ylabel("Number of flats", fontsize = 12, labelpad = 5)
    addlabels(categories , count)

    # Save and show
    plt.savefig('Overview_of_advertised_apartments.png')
    #plt.show()


# OVERVIEW COUNT PLOT ADVERTISED APARTMENTS IN SELECTED LOCATION
def overview_count_plot():
    # Create bar plot
    plt.figure(figsize=(11, 6))
    ax = sns.countplot(df, x="flat_type", hue="city")

    # Titles and labels
    plt.title("Number of advertised apartments in selected locations", fontsize = 16)
    plt.xlabel("Disposition of the apartment", fontsize = 12, labelpad = 5)
    plt.ylabel("Number of flats", fontsize = 12, labelpad = 5)
    
    for i in ax.containers:
        ax.bar_label(i)

    # Save and show
    plt.savefig('Number_of_advertised_apartments_in_selected_locations.png')
    #plt.show()


# BARPLOT COEFFICIENT OCCUPANCY
def barplot_occupancy_coefficient():   
    # Data
    grouped = df.groupby(['city', 'flat_type']).size().reset_index(name='count')
    count_list = grouped['count'].tolist()
    citis = grouped['city'].tolist()
    flats_disposition = grouped['flat_type'].tolist()
    population_city = [population[city] for city in citis]

    data = {
    'city': citis,
    'flat_type': flats_disposition,
    'count': count_list,
    'population': population_city
    }

    df_grouped = pd.DataFrame(data)

    df_grouped['coefficient'] = df_grouped['count'] / df_grouped['population']

    # Create bar plot
    plt.figure(figsize=(11, 6))
    bar_plot = sns.barplot(data=df_grouped, y="coefficient", x = 'flat_type', hue = 'city', hue_order = city_all)

    # Titles and labels
    bar_plot.axes.set_title("Bar plot of occupancy coefficient by apartment type and city",fontsize=16)
    bar_plot.set_xlabel("Flat type",fontsize=12)
    bar_plot.set_ylabel("Occupancy coefficient",fontsize=12)

    # Modify hue label
    legend = bar_plot.legend_
    legend.set_title("City")
    legend.get_title().set_fontsize(12)

    # Save and show
    plt.savefig('Barplot_coefficient_occupancy.png')
    #plt.show()


# BOXPLOT FLAT PRICE
def boxplot_flats_price():
    # Create box plot
    plt.figure(figsize=(11, 6))
    box_plot = sns.boxplot(data=df, y="price", x = 'flat_type', hue = 'city')

    # Titles and labels
    box_plot.axes.set_title("Boxplot prices by apartment type and city",fontsize=16)
    box_plot.set_xlabel("Flat type",fontsize=12)
    box_plot.set_ylabel("Price [CZK]",fontsize=12)

    # Modify hue label
    legend = box_plot.legend_
    legend.set_title("City")
    legend.get_title().set_fontsize(12)
    #plt.ticklabel_format(style='plain', axis='y',useOffset=False)

    # format the y-axis with spaces as thousand separators
    def thousands_formatter(x, pos):
        return f'{int(x):,}'.replace(',', ' ')
    box_plot.yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

    # Save and show
    plt.savefig('Boxplot_flats_price.png')
    #plt.show()

# BOXPLOT FLAT PRICE WITHOUT OUTLIERS
def boxplot_flats_price_no_outliers():
    # Create box plot
    plt.figure(figsize=(11, 6))
    box_plot = sns.boxplot(data=df, y="price", x = 'flat_type', hue = 'city', showfliers=False)

    # Titles and labels
    box_plot.axes.set_title("Boxplot prices by apartment type and city",fontsize=16)
    box_plot.set_xlabel("Flat type",fontsize=12)
    box_plot.set_ylabel("Price [CZK]",fontsize=12)

    # Modify hue label
    legend = box_plot.legend_
    legend.set_title("City")
    legend.get_title().set_fontsize(12)
    #plt.ticklabel_format(style='plain', axis='y',useOffset=False)

    # Format the y-axis with spaces as thousand separators
    def thousands_formatter(x, pos):
        return f'{int(x):,}'.replace(',', ' ')
    box_plot.yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

    # Save and show
    plt.savefig('Boxplot_flats_price_no_outliers.png')
    #plt.show()


# BARPLOT FLAT PRICE 
def barplot_flats_price():
    # Create bar plot
    plt.figure(figsize=(11, 6))
    bar_plot = sns.barplot(data=df, y="price", x = 'flat_type', hue = 'city')

    # Titles and labels
    bar_plot.axes.set_title("Barplot prices by apartment type and city",fontsize=16)
    bar_plot.set_xlabel("Flat type",fontsize=12)
    bar_plot.set_ylabel("Price [CZK]",fontsize=12)
    #plt.ticklabel_format(style='plain', axis='y',useOffset=False)

    # Format the y-axis with spaces as thousand separators
    def thousands_formatter(x, pos):
        return f'{int(x):,}'.replace(',', ' ')
    bar_plot.yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

    # Modify hue label
    legend = bar_plot.legend_
    legend.set_title("City")
    legend.get_title().set_fontsize(12)

    # Save and show
    plt.savefig('Barplot_flats_price.png')
    #plt.show()


# POINTPLOT FLAT PRICE
def pointplot_flats_price():
    # Create point plot
    plt.figure(figsize=(11, 6))
    point_plot = sns.pointplot(data=df, y="price", x = 'flat_type', hue = 'city')

    # Titles and labels
    point_plot.axes.set_title("Pointplot prices by apartment type and city",fontsize=16)
    point_plot.set_xlabel("Flat type",fontsize=12)
    point_plot.set_ylabel("Price [CZK]",fontsize=12)
    #plt.ticklabel_format(style='plain', axis='y',useOffset=False)

    # Format the y-axis with spaces as thousand separators
    def thousands_formatter(x, pos):
        return f'{int(x):,}'.replace(',', ' ')
    point_plot.yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

    # Modify hue label
    legend = point_plot.legend_
    legend.set_title("City")
    legend.get_title().set_fontsize(12)

    # Save and show
    plt.savefig('Pointplot_flats_price.png')
    #plt.show()

# HISTPLOT PRICE PER SQ METER
def histplot_price_sq_meter(): 
    # Create histogram
    plt.figure(figsize=(11, 6))
    hist_plot = sns.histplot(data=df, x='price_per_sq_meter', hue='city', bins= np.arange(0, 300000, 10000), kde=True, stat='density', common_norm=False, line_kws={"lw":4})

    # Range x axis
    hist_plot.set_xlim(0, 300000)

    # Titles and labels
    hist_plot.axes.set_title("Distribution of Square Meter Prices by City",fontsize=16)
    hist_plot.set_xlabel("Price per square m [CZK/m$^2$]",fontsize=12)
    hist_plot.set_ylabel("Density",fontsize=12)

    # Modify hue label
    legend = hist_plot.legend_
    legend.set_title("City")
    legend.get_title().set_fontsize(12)

    # Save and show
    plt.savefig('Histplot_kde_price_distribution.png')
    #plt.show()



def facegrid_price_sq_meter():
    # Create facegrid
    plt.figure(figsize=(11, 6))
    g = sns.FacetGrid(df, col="city")
    g.map_dataframe(sns.histplot, x="price_per_sq_meter", hue='city', bins= np.arange(0, 300000, 10000), stat='density', common_norm=False)

    # Titles and labels
    plt.setp(g.axes, xlabel='Price per square m', ylabel='Density')

    # Save and show
    plt.savefig('facegrid_price_distribution.png')
    #plt.show()


def barplot_price_sq_meter():
    # Data
    price_mean_sq_m = [int(df[df['city'] == city_choose]['price_per_sq_meter'].mean()) for city_choose in city_all] 

    # Create barplot
    plt.figure(figsize=(11, 6))
    plt.bar(city_all , price_mean_sq_m)

    # Titles and labels
    plt.title("Mean Price of Square Meter by City", fontsize = 16)
    plt.xlabel("City", fontsize = 12, labelpad = 5)
    plt.ylabel("Price per square m [CZK/m$^2$]", fontsize = 12, labelpad = 5)
    addlabels(city_all , price_mean_sq_m)

    # Save and show
    plt.savefig('Barplot_price_sq_meter.png')
    #plt.show()

def save_data_frame_price():
    df_save =  df.groupby(['city', 'flat_type'])['price'].describe()
    df_save.to_excel('data_price.xlsx')

def save_data_frame_price_sq_meter():
    df_save =  df.groupby(['city', 'flat_type'])['price_per_sq_meter'].describe()
    df_save.to_excel('data_price_sq_meter.xlsx')


if __name__ == "__main__":
    overview_bar_plot()
    overview_count_plot()
    barplot_occupancy_coefficient()
    boxplot_flats_price()
    boxplot_flats_price_no_outliers()
    barplot_flats_price()
    pointplot_flats_price()
    histplot_price_sq_meter()
    facegrid_price_sq_meter()
    barplot_price_sq_meter()

    save_data_frame_price()
    save_data_frame_price_sq_meter()
    