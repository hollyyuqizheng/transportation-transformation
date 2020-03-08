All Chicago taxi data was collected by Becky Mathew. 
----------------------------------------------------
I. Source 

This dataset contains information about taxi rides in Chicago in 2019. All the Chicago taxi data comes from the City of Chicago's official data portal. Data was collected using the SodaPy API, and the script for collection can be found in scripts/chicago/chicago_taxi.py. The full dataset is available at https://data.cityofchicago.org/Transportation/Taxi-Trips/wrvz-psew/data. If needed, we can collect data from earlier years from this site as well. 

----------------------------------------------------
II. Data format 

There are around 20 million rows for the year of 2019, where each row is a single taxi ride. This dataset is too large to show on GitHub, so I sampled a smaller dataset of 50,000 rows from January 1, 2019 and January 2, 2019 combined.

There are 22 columns (not counting the index) which are descriptors of the dataset. Full documentation of the dataset can be found at https://dev.socrata.com/foundry/data.cityofchicago.org/wrvz-psew. 

b. trip_id: String representing the unique id for this taxi ride, such as "1a17d83ac05d6f89ff6e0c03b47849e6f4e1099f"
c. taxi_id: String representing unique id for this taxi, such as "33eb8518952dbdc8a4c6648ad8fdf65dc84fac160f3d6fee95813377ebd66095d2862f1813b774f7a048d5a9aaea55aa02a223510027ee08a37485e1b784d104"
d. trip_start_timestamp: Floating timestamp representing the start time of the taxi ride (rounded to the nearest 15 minutes), such as 2019-01-01T00:00:00.000
e. trip_end_timestamp: Floating timestamp representing the end time of the taxi ride (rounded to the nearest 15 minutes), such as 2019-01-01T00:15:00.000
f. trip_seconds: Duration of the trip in seconds, such as 734
g. trip_miles: Distance of the trip in miles, such as 2.1
h. pickup_community_area: The number representing the community area where the trip began, such as 8
i. dropoff_community_area: The number representing the community area where the trip ended, such as 8 
j. fare: fare of this trip, such as 9.25
k. tips: Customer's tip paid, such as 2.05
l. extras: Extra charges, such as 1
m. trip_total: Total cost of the trip, such as 12.3
n. payment_type: String method of payment, such as "Credit Card"
o. company: String name of taxi company, such as "Yellow Cab"
p. pickup_centroid_latitude: The latitude of the center of the pickup census tract or community area, such as 41.89960211
q. pickup_centroid_longitude: The longitude of the center of the pickup census tract or community area, such as -87.63330804
r. pickup_centroid_location: pickup_centroid_latititude and pickup_centroid_longitude combined into a point datatype, such as {'type': 'Point', 'coordinates': [-87.6333080367, 41.899602111]}
s. dropoff_centroid_latitude: The latitude of the center of the dropoff census tract or community area, such as 41.89960211
t. dropoff_centroid_longitude: The longitude of the center of the dropoff census tract or community area, such as -87.63330804
u. dropoff_centroid_location: dropoff_centroid_latititude and dropoff_centroid_longitude combined into a point datatype, such as {'type': 'Point', 'coordinates': [-87.6333080367, 41.899602111]}
v. pickup_census_tract: String of the census tract where the taxi picked up the rider (sometimes omitted for privacy), such as 7031081800
w. dropoff_census_tract: String of the census tract where the taxi dropped off the customer (sometimes omitted for privacy), such as 17031081000
x. tolls: Tolls for this trip, such as 0

----------------------------------------------------
III. Exploring the data

We did some basic exploratory statistics on the dataset. In data/chicago/chi_taxi_2019_01_daily_ridership.json, you can see descriptive statistics about the mean, min, max, etc. of ridership counts per day. In data/chicago/pickups_histogram.csv, you can see the amount of pickups (for 01/01/2019 and 01/02/2019) per community area. Areas in the Loop (business and tourism) or near the airport have many more taxi rides than neighborhoods on the outskirts of Chicago. 

