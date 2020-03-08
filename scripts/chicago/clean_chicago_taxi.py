#!/usr/bin/env python3
import pandas as pd
import json

data = pd.read_csv("C:\\Users\\CodeB\\Documents\\GitHub\\transportation-transformation\\data\\chicago\\chicago_taxi_2019_01.csv")
df = pd.DataFrame(data)
# usecols=["trip_start_timestamp", "trip_end_timestamp", "trip_seconds", "trip_miles", "fare", "tips", "tolls", "extras", "trip_total",  "pickup_centroid_latitude", "pickup_centroid_longitude", "dropoff_centroid_latitude", "dropoff_centroid_longitude"]

# Drop NAs for pickup / dropoff lat-lon. Drops 203 rows (from 2000 rows to 1797 rows)
df_no_na = df.dropna(subset=["pickup_centroid_latitude", "pickup_centroid_longitude", "dropoff_centroid_latitude", "dropoff_centroid_longitude"])
print(df_no_na.shape)

# Split timestamp into date and time columns
df = df.assign(trip_start_date=df['trip_start_timestamp'].str[:10])
df = df.assign(trip_start_time=df['trip_start_timestamp'].str[11:])
df = df.assign(trip_end_date=df['trip_end_timestamp'].str[:10])
df = df.assign(trip_end_time=df['trip_end_timestamp'].str[11:])

# Group by date and count
date_df = df.groupby(["trip_start_date"]).count()

# Daily ridership descriptive statistics (mean, std, min, max, etc)
desc_stats = date_df["trip_end_date"].describe()
print("daily ridership descriptive stats: ", desc_stats)

duplicated = df.duplicated()
print(duplicated.value_counts())

desc_stats_dict = desc_stats.to_dict()
with open("chi_taxi_2019_01_daily_ridership.json", "w") as fout:
    json.dump(desc_stats_dict, fout)

# TODO: output format?
# TODO: Drop census tracts, community areas, tips, tolls, extras, payment_type, locations, computed region, company
