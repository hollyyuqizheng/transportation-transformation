I. Source: 
  This data comes from a public table which can be found at https://www.newyork-demographics.com/zip_codes_by_population
  The information from this table has the following citation:
      United States Census Bureau. B01001 SEX BY AGE, 2018 American Community Survey 5-Year Estimates. U.S. Census Bureau, American Community Survey Office. Web. 19 December 2019. http://www.census.gov/.
  
  I also joined this data with a chart from http://zipatlas.com/us/ny/zip-code-comparison/population-density.16.htm to add
  a latitude and longitude column to the original dataset.
   
   We modified our dataset from the original in that in the original there was one row per rank so some rows represented multiple zip codes. We separated the zipcodes so that there are multiple rows with the same rank but each row only represents
one zipcode. This will make it easier to join the data with other data sets by zipcode. But, in joining the two datasets there
were some rows that got dropped because I think there were some zipcodes that were not common between the two datasets. 
      
------------------------------------------------------------------------

II. Data Format:
    The full dataset contains 1589 rows, one for each zipcode that is represented. Each row shows the rank among the rest 
    of the zipcodes, zipcode, population for that zipcode and the latitude and longitude for that code. 
    
    Columns:
      - Rank: The zipcodes rank amongst the rest of the zip codes in the dataset. Multiple zip codes with the same population
        will tie for a rank, so some zip codes/rows have the same rank. There are 1754 rows but 1605 ranks.
      - Zip_Code: A 5 digit zip codes
      - lat_long: coordinates for the latitude and longitude of the zip code area, to the 6th decimal point
      - Population: A zip code's total population.
      
The sample dataset contains 5 rows from throughout the total dataset in intervals of about 350 rows.
