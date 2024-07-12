# Analysis of Advertised Apartment Prices in the Czech Republic

This program aims to analyze the advertised prices of apartments with different dispositions (1+kk, 2+kk, 3+kk) in the largest cities of the Czech Republic: Prague, Brno, Ostrava, and Olomouc. The analysis will provide insights into the price trends and differences across these cities.

## Analysis parameters

**Dispositions**
* 1+kk: One room with a kitchenette
* 2+kk: Two rooms with a kitchenette
* 3+kk: Three rooms with a kitchenette

**Cities**
Prague: The capital and largest city of the Czech Republic
Brno: The second-largest city and a significant cultural and economic center
Ostrava: The third-largest city, known for its industrial background
Olomouc: The sixth-largest city, with a rich historical and cultural heritage

## User settings
The user can customize the analysis parameters by modifying the selection of cities and apartment dispositions. To adjust these settings, update the following variables:

* 'city_all': Specifies the cities to be included in the analysis.
* 'flat_type': Specifies the apartment dispositions to be included in the analysis.

# Analysis 
The method of analyzing all available data was employed because the data set was not extensive enough to necessitate sampling. This approach ensured that the results are based on the entirety of the available information, thereby minimizing the risk of bias and providing the most accurate and comprehensive insights possible.

This analysis processed a total of XXX apartments. However, some advertisements do not provide the price of the property and have therefore been excluded from this analysis. The number of properties analysed and the number of incompletely advertised properties is shown below.

![Overview_of_advertised_apartments](https://github.com/Libre89/Apartment_price_analysis/assets/101059017/57779619-1022-41b7-9d35-1cf321973ecb)

The following chart shows the number of advertised apartments in the selected locations.

![Number_of_advertised_apartments_in_selected_locations](https://github.com/Libre89/Apartment_price_analysis/assets/101059017/ea151214-a2d3-4897-b9c8-f09562926cd8)

The next chart is a boxplot showing the distribution of apartment prices in selected locations and dispositions. This boxplot allows us to quickly compare the price spread of apartments between different locations and types of dispositions and identify any trends or deviations.

![Boxplot_of_flats](https://github.com/Libre89/Apartment_price_analysis/assets/101059017/9ab6d251-6e9d-46b0-b686-995f76f1a7a5)

The following barplot shows average house prices with a 95% confidence interval.

![Barplot_of_flats](https://github.com/Libre89/Apartment_price_analysis/assets/101059017/3ae8e20a-3333-44b1-974c-a7072c719d2b)

The pointplot shows the same data as the previous boxplot, but it also shows a comparison of price growth for different apartment layouts. 

![Pointplot_of_flats](https://github.com/Libre89/Apartment_price_analysis/assets/101059017/b81b90dc-8acd-4e7e-b254-ccc1fa9de57f)

The following histogram with kernel density estimate (KDE) plot shows the the price per square meter of housing in the selected cities.

![histplot_of_flats](https://github.com/Libre89/Apartment_price_analysis/assets/101059017/2747296f-2d1a-4727-9c7a-1401c3a825d8)

# Conclusion 




