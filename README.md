# Analysis of Advertised Apartment Prices in the Czech Republic

This program aims to analyze the advertised prices of apartments with different dispositions (1+kk, 2+kk, 3+kk) in the largest cities of the Czech Republic: Prague, Brno, Ostrava, and Olomouc. The analysis will provide insights into the price trends and differences across these cities.

## Analysis parameters

**Dispositions**
* 1+kk: One room with a kitchenette
* 2+kk: Two rooms with a kitchenette
* 3+kk: Three rooms with a kitchenette

**Cities**
* Prague: The capital and largest city of the Czech Republic
* Brno: The second-largest city and a significant cultural and economic center
* Ostrava: The third-largest city, known for its industrial background
* Olomouc: The sixth-largest city, with a rich historical and cultural heritage

## User settings
The user can customize the analysis parameters by modifying the selection of cities and apartment dispositions. To adjust these settings, update the following variables:

* 'city_all': Specifies the cities to be included in the analysis.
* 'flat_type': Specifies the apartment dispositions to be included in the analysis.

# Analysis 
In this analysis, a full dataset analysis was used, examining all available data due to the dataset's manageable size, which did not necessitate sampling. This method ensures that the results are based on the entirety of the available information, thereby minimizing the risk of bias and providing the most accurate and comprehensive insights possible.

A total of XXX apartments were processed. However, some advertisements did not provide the price of the property and were therefore dropped from this analysis. The number of properties analyzed and the number of incompletely advertised properties are shown below.
* Number of advertisements with a price: XXX
* Number of advertisements without a price: XXX

![Overview_of_advertised_apartments](https://github.com/Libre89/Apartment_price_analysis/assets/101059017/57779619-1022-41b7-9d35-1cf321973ecb)

The following chart shows the number of advertised apartments  across selected locations, categorized by apartment dispositions. Prague has the highest number of advertised apartments for all dispositions, significantly higher compared to the other cities analyzed. Notably, Ostrava, despite being the third largest city in the Czech Republic, has the fewest advertisements, particularly for 1+kk and 2+kk apartments.

![Number_of_advertised_apartments_in_selected_locations](https://github.com/Libre89/Apartment_price_analysis/assets/101059017/ea151214-a2d3-4897-b9c8-f09562926cd8)

To provide a more meaningful analysis of apartment availability, a new graph has been created which depicts the occupancy coefficient (number of availbe flat / population of the city). This coefficient is calculated by dividing the number of available apartments by the population of each city, offering a clearer picture of apartment accessibility relative to city size.

The bar plot shows that Olomouc has the highest occupancy coefficients across all apartment types (1+kk, 2+kk, 3+kk), indicating better apartment availability relative to its population.

* occupancy coeffcient = number of availbe flat / population of the city

![Barplot_coefficient_occupancy](https://github.com/user-attachments/assets/cd6a311e-a8f5-4cdf-9503-685180bbd75d)

The next graph is a boxplot that clearly illustrates the distribution of apartment prices. This visualization helps to understand the spread of prices in each city, highlighting variations and outliers.

![Boxplot_of_flats](https://github.com/user-attachments/assets/28bac1c1-f2d3-4320-bbd4-e88274f7a3da)

The following graph is also a boxplot but excludes outliers and presents the data from the previous graph in more detail.

![Boxplot_of_flats_no_outliers](https://github.com/user-attachments/assets/4107743f-0133-4943-8ec5-bbeb7da4340d)

The following barplot shows average apartment prices. This barplot includes a 95% confidence interval for each average price, indicating the range within which we can be 95% confident that the true average lies. 

![Barplot_of_flats](https://github.com/user-attachments/assets/0c4c39ae-9714-45ee-9d23-68cc23addee2)

The pointplot shows the same data as the previous boxplot, but it also shows a comparison of price growth for different apartment layouts. The pointplot shows a near-linear trend in apartment prices increasing with larger flat types across all cities, with a slightly steeper rise between 2+kk and 3+kk apartments in Prague.

![Pointplot_of_flats](https://github.com/user-attachments/assets/7767a186-57b4-4097-894d-d1e383dd80e2)

However, comparing apartment prices based on dispositions alone does not fully capture the price differences between cities. The following histogram with a Kernel Density Estimate (KDE) provides a more detailed view by showing the price per square meter of apartments in various cities.

![histplot_of_flats](https://github.com/user-attachments/assets/9c2defa8-d8e7-4eb6-9fa9-7754ef5b9be6)

## Summary statistic
* Price summary statistic
* 
|     | Flat  |                | mean          | std       | min       | 25%        | 50%        | 75%        | max       |
| City    | Flat disposition | Count          |               |           |           |            |            |            |           |
| Praha   | 1+kk             | x
| Praha   | 2+kk             |
| Praha   | 3+kk             |
| Brno    | 1+kk             |
| Brno    | 2+kk             |
| Brno    | 3+kk             |
| Ostrava | 1+kk             |
| Ostrava | 2+kk             |
| Ostrava | 3+kk             |
| Olomouc | 1+kk             |
| Olomouc | 2+kk             |
| Olomouc | 3+kk             |

* Price per sq meter summary statistic

|         |                  |
| City    | Flat disposition |
| -----   | --------         |
| Praha   | 1+kk             |
| Praha   | 2+kk             |
| Praha   | 3+kk             |
| Brno    | 1+kk             |
| Brno    | 2+kk             |
| Brno    | 3+kk             |
| Ostrava | 1+kk             |
| Ostrava | 2+kk             |
| Ostrava | 3+kk             |
| Olomouc | 1+kk             |
| Olomouc | 2+kk             |
| Olomouc | 3+kk             |

XXX
RATIO POČET BYTŮ NA POČET OBYVATEL !!!

XXX

The next chart is a boxplot showing the distribution of apartment prices in selected locations and dispositions. This boxplot allows us to quickly compare the price spread of apartments between different locations and types of dispositions and identify any trends or deviations.

![Boxplot_of_flats](https://github.com/Libre89/Apartment_price_analysis/assets/101059017/9ab6d251-6e9d-46b0-b686-995f76f1a7a5)

The following barplot shows average house prices with a 95% confidence interval.

![Barplot_of_flats](https://github.com/Libre89/Apartment_price_analysis/assets/101059017/3ae8e20a-3333-44b1-974c-a7072c719d2b)

The pointplot shows the same data as the previous boxplot, but it also shows a comparison of price growth for different apartment layouts. 

![Pointplot_of_flats](https://github.com/Libre89/Apartment_price_analysis/assets/101059017/b81b90dc-8acd-4e7e-b254-ccc1fa9de57f)

The following histogram with kernel density estimate (KDE) plot shows the the price per square meter of housing in the selected cities.

![histplot_of_flats](https://github.com/Libre89/Apartment_price_analysis/assets/101059017/2747296f-2d1a-4727-9c7a-1401c3a825d8)

# Conclusion 




