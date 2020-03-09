I. Source: 
  This data comes from a public table which can be found at https://www.newyork-demographics.com/zip_codes_by_population
  The information from this table has the following citation:
      United States Census Bureau. B01001 SEX BY AGE, 2018 American Community Survey 5-Year Estimates. U.S. Census Bureau, American Community Survey Office. Web. 19 December 2019. http://www.census.gov/.
      
------------------------------------------------------------------------

II. Data Format:
    The full dataset contains 1754 rows, one for each zipcode that is represented. Each row shows the rank among the rest 
    of the zipcodes, zipcode and population for that zipcode.
    
    Columns:
      - Rank: The zipcodes rank amongst the rest of the zip codes in the dataset. Multiple zip codes with the same population
        will tie for a rank, so some zip codes/rows have the same rank. There are 1754 rows but 1605 ranks.
      - Zipcode: A 5 digit zip codes
      - Population: A zip code's total population.
      
The sample dataset contains 5 rows from throughout the total dataset in intervals of about 350 rows.
