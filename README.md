# Housing_Price_Chloropleth

The objective of this project was to visualize percent change in average real estate prices on nation wide and state wide choropleth maps from 2010 to 2019. Percent change was measured on a year to year basis as well as total percent change accrued during the decade from a base line year (2010). Presenting the data in this way would allow an intuitive view of real asset growth in the United States, with the option of "zooming in" to the state level to see which counties drove those price changes.

Two separate datasets were needed to accomplish the descriptive analysis. The first was a list of housing prices with accompanying state, county and monthly pricing information, which was downloaded from Zillow. The second was a list of yearly population estimates on both the state and county level, which was procured from the US Census website. 

The greatest limitation in the data is the lack of price observations for certain counties in the earlier years of the Zillow dataset. For certain states like South Dakota or Mississippi, numerous counties had no observations up to as late as 2017, likely due to a combination of Zillow being an emerging platform for real estate listings in the early 2010s and a lack of listings in general, as missing data often comes from less populous states. This absence will likely cause large swings in the percent change due to relatively fewer data points. The census data was comprehensive, though each year was a population estimate since the census is only taken every ten years. The study was limited to 2010-2019 due to way the census data is stored and recorded, however the missing data issue with the Zillow data from they time frame would have been even more acute. 

Using a combination of pandas, base python, and numpy, census data was cleaned such that each row contained a single observation (a population for a given state/county/year). Using the state population estimate for a given year, the proportion of the state's population, for a given county, for a given year, was measured. The Zillow data was cleaned and grouped such that each row contained a single observation (an average price for a given state/county/year). 

Using the state, county, and year as a key, the datasets were joined. Using the state population proportion, each county's price was weighted to represent the relative number of people affected by that price. This weighted price was summed by state to get the weighted average price of real estate for a state in a given year. Using this weighted price the percent change in price was calculated from year to year, and cumulative percent change in price from the 2010 baseline price.

For the county level data, each observation was already grouped with the merged datasets. Additionally, since the objective was to get the percent price change within a county, percent change on the county level was calculated with the average price, not the price weighted by the state population. The percent change was calculated between the average real estate prices for counties from year to year and the cumulative percent change in price from the 2010 baseline price.

Additional datasets were required to take the aggregated information and display it in choropleth maps. geojson files which contained latitudinal and longitudinal data representing the coordinates for counties and states were used in conjunction with the plotly package to draw counties and states on a blank map of the US. Additionally a FIPS data set which encoded the state and counties into numeric codes was used as an intermediary to join the aggregate price data and the geographic coordinates. The FIPS was joined to the pricing data on the state and county fields, and the resulting dataset was then joined to the geographic data via the FIPS code field. From that aggregated data frame a choropleth map could be generated using the choropleth package.

Four separate choropleth maps scripts were generated for data. For the continental US, an animated map was generated to show year-to-year percent change in real estate price, where darker shades indicated a larger percent increase in price from the previous year. An additional map was generated which displays the total percent change in the price from the 2010 baseline, where darker shades indicated a larger percent increase. For each US state, an animated map was generated to show year-to-year percent change in real estate price, where darker shades indicated a larger percent increase in price from the previous year. An additional map was generated which displays the total percent change in the price from the 2010 baseline, where darker shades indicated a larger percent increase. 



One potential avenue for more precise analysis could be to alter how the statewide population prices were weighted. The prices in this study are weighted by the proportion of the state populations, but another aspect real estate pricing relates to how populous a state is compared to the country as a whole. A certain county could be weighted heavily based on the proportion of state population that lives there, but could be in a relatively less populated state, distorting the relevancy of that price with a larger proportion of a smaller number of people than a more populous state. 