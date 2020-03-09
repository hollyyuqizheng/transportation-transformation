New York City Yellow Taxi Trip data was collected by Melia Okura and Becky Mathew. 
----------------------------------------------------------------------------------
I. Source 
This dataset contains ridership information from a Freedom of Information Law request on the New York Taxi and Limousine Commission. The full dataset is too large to host on GitHub, but you can access it at https://drive.google.com/file/d/1DwtqPVg_EgN4x7gevIHhBvR-wzmnCiBb/view?usp=sharing. The original data did not have the latitude and longitude data, which we added using scripts/new_york/nyc_taxi_zone_shapefile.py

----------------------------------------------------------------------------------
II. Data format

There are roughly 44 million rows, where each row describes a taxi ride using the Yellow Taxi company in New York City in 2018. 

The data dictionary describing this dataset can be found at https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf.

- VendorID: code indicating the TPRP provider that provided the record
- tpep_pickup_datetime: date and time the meter was engaged
- tpep_dropoff_datetime: date and time the meter was disengaged
- passenger_count: the number of passengers in vehicle
- trip_distance: elapsed distance reported by taxi monitor
- PULocationID: TLC Taxi Zone in which the taximeter was engaged
- DOLocationID: TLC Taxi Zone in which the taximeter was disengaged
- PUlatitude: Centroid latitude of TLC taxi zone in which the taximeter was engaged
- PUlongitude: Centroid longitude of TLC taxi zone in which the taximeter was engaged
- DOlatitude: Centroid latitude of TLC taxi zone in which the taximeter was disengaged
- DOlongitude: Centroid longitude of TLC taxi zone in which the taximeter was disengaged
- rateCodeID: the final rate code in effect at the end of the trip
- store_and_fwd_flag: flag indicator for whether the trip record was held in the vehicle memory before sending to the vendor
- payment_type: A numeric code signifying how the passenger paid for their trip
- fare_amount: time-and-distance fare calculated by the meter
- Extra: miscellaneous extras and surcharges
- MTA_Tax: MTA tax that is automatically triggered based on the metered rate in use
- improvement_charge: improvement surcharge assessed trips at the flag drop.
- tip_amount: The tip amount (for credit card payment only)
- tolls_amount: Total amount of tolls paid on the trip
- total_amount: Total cost of the trip
- congestion_surcharge: This is in the data, but not in the data dictionary so we're not sure what it is. It's most likely not relevant to our stats, since we only care about lat/lon and time. 