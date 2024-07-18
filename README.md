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

A total of 3426 apartments were processed. However, some advertisements did not provide the price of the property and were therefore dropped from this analysis. The number of properties analyzed and the number of incompletely advertised properties are shown below.
* Number of advertisements with a price: 3277
* Number of advertisements without a price: 149

![Overview_of_advertised_apartments](https://github.com/user-attachments/assets/65dfadbe-601e-4ada-8979-ff72b1a87f02)

The following chart shows the number of advertised apartments  across selected locations, categorized by apartment dispositions. Prague has the highest number of advertised apartments for all dispositions, significantly higher compared to the other cities analyzed. Notably, Ostrava, despite being the third largest city in the Czech Republic, has the fewest advertisements, particularly for 1+kk and 2+kk apartments.

![Number_of_advertised_apartments_in_selected_locations](https://github.com/user-attachments/assets/06b6b4d0-95a7-4eb8-836f-f971c1fd4452)

To provide a more meaningful analysis of apartment availability, a new graph has been created which depicts the occupancy coefficient (number of availbe flat / population of the city). This coefficient is calculated by dividing the number of available apartments by the population of each city, offering a clearer picture of apartment accessibility relative to city size.

The bar plot shows that Olomouc has the highest occupancy coefficients across all apartment types (1+kk, 2+kk, 3+kk), indicating better apartment availability relative to its population.

* occupancy coeffcient = number of availbe flat / population of the city

![Barplot_coefficient_occupancy](https://github.com/user-attachments/assets/70fa2442-d11f-46a2-a624-59bd380792f4)

The next graph is a boxplot that clearly illustrates the distribution of apartment prices. This visualization helps to understand the spread of prices in each city, highlighting variations and outliers.

![Boxplot_flats_price](https://github.com/user-attachments/assets/0d36020c-08bf-4618-8c5e-93b3d4332374)

The following graph is also a boxplot but excludes outliers and presents the data from the previous graph in more detail.

![Boxplot_flats_price_no_outliers](https://github.com/user-attachments/assets/318a53ce-2fc6-4ac2-bbee-b01c3b8ef582)

The following barplot shows average apartment prices. This barplot includes a 95% confidence interval for each average price, indicating the range within which we can be 95% confident that the true average lies. 

![Barplot_flats_price](https://github.com/user-attachments/assets/1a73c70e-0fec-4cbc-a377-375c0ed9fcf6)

The pointplot shows the same data as the previous boxplot, but it also shows a comparison of price growth for different apartment layouts. The pointplot shows a near-linear trend in apartment prices increasing with larger flat types across all cities, with a slightly steeper rise between 2+kk and 3+kk apartments in Prague.

![Pointplot_flats_price](https://github.com/user-attachments/assets/9f67c33e-a8d7-49f6-bb90-3d9abd271f1a)

However, comparing apartment prices based on dispositions alone does not fully capture the price differences between cities. The following histogram with a Kernel Density Estimate (KDE) provides a more detailed view by showing the price per square meter of apartments in various cities.

![histplot_kde_price_distribution](https://github.com/user-attachments/assets/cba6d641-0113-4b88-a261-9d5309dafc25)


## Summary statistic
* Price summary statistic

| City    | Flat disposition | Count          | Mean          | Std        | Min       | 25%        | 50%        | 75%        | Max       |
| -----   | -----            | -----          | -----         | -----      | -----     | -----      | -----      | -----      | -----     |
| Praha   | 1+kk             | 472            | 5374513.60    | 1690742.93 |1435000    | 4309420    | 5390000    |6300000     |17390000   |
| Praha   | 2+kk             | 1020           | 7647326.82    | 3146646.58 |550000     | 6199750    | 7348700    |8590000     |52900000   |
| Praha   | 3+kk             | 826            | 11874193.21   | 4515974.32 |1987000    | 9292500    | 11000000   |13474225    |57500000   |
| Brno    | 1+kk             | 132            | 4339260.60    | 922916.50  |2290000    | 3699750    | 4219000    |4931635     |6990000    |
| Brno    | 2+kk             | 173            | 6545981.99    | 1492258.44 |3675000    | 5500000    | 6390000    |7362500     |11900000   |
| Brno    | 3+kk             | 129            | 9454796.13    | 1960506.82 |5500000    | 7990000    | 9300000    |10929000    |15100000   |
| Ostrava | 1+kk             | 14             | 1804865.64    | 552142.84  |389120     | 1670000    | 1999000    |1999000     |2846700    |
| Ostrava | 2+kk             | 34             | 3802867.94    | 1534555.93 |360680     | 2800000    | 3761702    |4824670     |8300000    |
| Ostrava | 3+kk             | 65             | 5411165.53    | 3252119.84 |2390000    | 3250000    | 4250000    |6990000     |18100000   |
| Olomouc | 1+kk             | 65             | 3430568.15    | 438650.42  |2020000    | 3150000    | 3400000    |3650000     |4490000    |
| Olomouc | 2+kk             | 127            | 5463026.83    | 917005.06  |2780000    | 4925000    | 5390000    |5810375     |9776500    |
| Olomouc | 3+kk             | 86             | 7797458.30    | 1984240.46 |4080000    | 6705000    |7467000     |8315000     |18990000   |

* Price per sq meter summary statistic
  
| City    | Flat disposition | Count          | Mean          | Std        | Min       | 25%        | 50%        | 75%        | Max       |
| -----   | -----            | -----          | -----         | -----      | -----     | -----      | -----      | -----      | -----     |
| Praha   | 1+kk             | 472            | 158316.02     | 43970.89   | 36530     | 136189     | 160500     | 178131     | 399437    |
| Praha   | 2+kk             | 1020           | 142476.96     | 39532.36   | 11299     | 121084     | 141510     | 163037     | 424390    |
| Praha   | 3+kk             | 826            | 139782.76     | 35400.75   | 24900     | 117896     | 139791     | 160075     | 471311    |
| Brno    | 1+kk             | 132            | 123689.06     | 22618.46   | 59800     | 113131     | 120312     | 135208     | 211402    |
| Brno    | 2+kk             | 173            | 116256.36     | 25436.20   | 54210     | 101666     | 118809     | 132682     | 196491    |
| Brno    | 3+kk             | 129            | 113672.19     | 22680.38   | 65625     | 96352      | 112777     | 122717     | 175581    |
| Ostrava | 1+kk             | 14             | 61898.88      | 21005.91   | 11791     | 50295      | 69465      | 74550      | 91829     |
| Ostrava | 2+kk             | 34             | 68069.32      | 20144.36   | 8015      | 60581      | 69922      | 81783      | 94150     |
| Ostrava | 3+kk             | 65             | 61510.07      | 21975.00   | 35691     | 46428      | 56578      | 72237      | 137121    |
| Olomouc | 1+kk             | 65             | 105335.92     | 11596.10   | 85384     | 96861      | 103000     | 108285     | 137931    |
| Olomouc | 2+kk             | 127            | 98282.63      | 13042.44   | 55600     | 91642      | 97483      | 103975     | 131276    |
| Olomouc | 3+kk             | 86             | 97797.66      | 20422.12   | 50287     | 85200      | 96953      | 107066     |171081     |
