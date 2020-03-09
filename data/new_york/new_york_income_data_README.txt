The data presented in this file illustrates income demographics for the city of New York. 

This data was obtained from 
- Manhattan: http://zipatlas.com/us/ny/new-york/zip-code-comparison/median-household-income.htm 
- Brooklyn: http://zipatlas.com/us/ny/brooklyn/zip-code-comparison/median-household-income.htm
- Bronx: http://zipatlas.com/us/ny/bronx/zip-code-comparison/median-household-income.htm
- Staten Island: http://zipatlas.com/us/ny/staten-island/zip-code-comparison/median-household-income.htm
- Queens: https://statisticalatlas.com/county-subdivision/New-York/Queens-County/Queens/Household-Income
All of these websites have compiled information from the 2010 census to produce their metrics.

The format of the income demographics in the csv file is as follows: 
Columns: 
	- Zip Code
	- Latitude and Longitude represented as lat #,long #
	- Location (i.e borough of NYC)
	- Average household income for this zip code

While this information may have significantly changed since 2010, we will use this information to normalize information about transportation density and accessibility because it is representative of income disparities and general inequality which can inform our analysis. Moreover, the expansion of NYC subway lines may have an impact on income demographics as gentrification increases.

Missing data was obtained from Statistical Atlas which also sourced income information from the 2010 census. Moreover, some zip codes with no information represented extremely small areas such as a building or block and were always encompassed by a larger zip code. Therefore, these smaller zip codes were deleted. The zip codes in the dataset should still represent comprehensive coverage of the city. The only other outlier is the World Trade Center, which has its own zip code, and accordingly an average household income of 0.