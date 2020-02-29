bart-2016.csv;  bart-2017.csv [downloaded]
source: downloaded from https://www.kaggle.com/saulfuh/bart-ridership
BART ridership data
-- headers: Origin,Destination,Throughput,DateTime
-- Number of passengers (Throughput) that went between two stations (Origin and Destination) in a given time (DateTime)
-- bart-2016: 9971582 lines; bart-2017: 3313625 lines


bart_station_info_short.csv [downloaded]
source: downloaded from https://www.kaggle.com/saulfuh/bart-ridership
Station Info for BART stations
-- headers: Abbreviation,Description,Location,Name


BART API [api call]
api calls to: http://api.bart.gov/docs/overview/index.aspx
-- more detailed info on stations (longitude/latitude instead of address)
-- station list + info stored in bart_station_list.json


bart_station_list_cleaned.tsv [created]
--- Tab-separated; columns are: station_abbreviation, longitude, latitude
--- cleaned from bart_station_list.json, which was from BART API;
didn't do anything fancy, just cut out certain entries from api output

bart_2016_cleaned.tsv [created]
--- 9971540 entries in total, right now it is sorted based on origin alphabetically
--- 42 entries with WSPR that was thrown out because WSPR is not in bart_station_list.json
--- utilized bart_station_list_cleaned.tsv to add in long/lat for each ridership data




st_taxi_stand.txt [scraped]
source: scraped from https://www.sfmta.com/getting-around/taxi/taxi-stand-list
-- address of taxi stands in sf, 76 stations in total, all unique


uber_movement_caltrain.csv [downloaded]
source: https://www.kaggle.com/vaishalij/san-francisco-caltrain-uber-movement-data
Aggregated Uber rides from Caltrain station in SF to other locations
-- headers: "Origin Movement ID",
            "Origin Display Name",
            "Destination Movement ID",
            "Destination Display Name",
            "Date Range",
            "Mean Travel Time (Seconds)",
            "Range - Lower Bound Travel Time (Seconds)",
            "Range - Upper Bound Travel Time (Seconds)"
