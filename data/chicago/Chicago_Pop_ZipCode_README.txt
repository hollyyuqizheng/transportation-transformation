I. Source: 
  This data comes from a public table which can be found at http://zipatlas.com/us/il/chicago/zip-code-comparison/population-density.htm
  The full dataset at this website contains other columns, but in our dataset I only included relevant columnns.
  This information is taken from the 2010 Census.
      
------------------------------------------------------------------------

II. Data Format:
    The full dataset contains 55 rows, one for each zipcode that is represented. Each row shows the rank among the rest 
    of the zipcodes based on population per square mile, logitude, latitude, zipcode and population for that zipcode.
    
    Columns:
      - Rank: The zipcodes rank amongst the rest of the zip codes in the dataset. The rank is determined by population
        per sqaure miles. There is only one zipcode per rank. 
      - Zipcode: A 5 digit zip codes
      - Logitude/latitude; longitude and latitude of zip code with 6 decimal places
      - Population: A zip code's total population.
