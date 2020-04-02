#!/usr/bin/env python3

# Get New York data per day
import pandas as pd
import math
import pickle
import json

# Load New York zipcode data
zipcode_data = pd.read_csv("C:\\Users\\CodeB\\Documents\\GitHub\\transportation-transformation\\data\\new_york\\NY_Pop_Zip_long_lat.csv")
zipcode_df = pd.DataFrame(zipcode_data)
# Dropping unnamed columns at end
zipcode_df = zipcode_df.iloc[:, 1:4]

# Split latlon column into two
lats = []
lons = []
for pair in zipcode_df["lat_long"]:
    lat_lon = pair.split(",")
    lats.append(float(lat_lon[0]))
    lons.append(float(lat_lon[1]))
zipcode_df["lat"] = lats
zipcode_df["lon"] = lons

# Dictionary of community areas to zipcode
latlon_to_zipcode = {}

def get_zipcode(lat, lon):
    """
    Given a latitude and longitude, find the closest zipcode.

    Distance is not the real-world distance, but Euclidean distance of lat-lon coordinates.
    """
    if latlon_to_zipcode.get((lat, lon)) == None:
        min_zip = None
        min_dist = float("inf")
        for idx, row in zipcode_df.iterrows():
            dist = math.sqrt((row["lat"] - float(lat)) ** 2 + (row["lon"] - float(lon)) ** 2)
            if dist < min_dist:
                min_zip = row["Zip_Code"]
                min_dist = dist

        latlon_to_zipcode[(lat, lon)] = min_zip
        with open("latlon_to_zipcode.pickle", "wb") as fout:
            pickle.dump(latlon_to_zipcode, fout)
        return min_zip
    else:
        return latlon_to_zipcode[(lat, lon)]

# Dictionary of zipcode to dictionary of month to frequency
# For example: {60601: {1: 50, 2: 25, ...}, ...}
pickup_zipcode_to_month_freq = {}
dropoff_zipcode_to_month_freq = {}

def insert_trip(row):
    """
    Take a df of taxi records for a single day and inserts it into zipcode_to_month_freq.
    """
    month = row["month"]
    pickup_zipcode = get_zipcode(row["PUlatitude"], row["PUlongitude"])
    dropoff_zipcode = get_zipcode(row["DOlatitude"], row["DOlongitude"])

    if pickup_zipcode_to_month_freq.get(pickup_zipcode) == None:
        pickup_zipcode_to_month_freq[pickup_zipcode] = {"01": 0, "02": 0, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0, "09": 0, "10": 0, "11": 0, "12": 0}
    pickup_zipcode_to_month_freq[pickup_zipcode][month] += 1

    if dropoff_zipcode_to_month_freq.get(dropoff_zipcode) == None:
        dropoff_zipcode_to_month_freq[dropoff_zipcode] = {"01": 0, "02": 0, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0, "09": 0, "10": 0, "11": 0, "12": 0}
    dropoff_zipcode_to_month_freq[dropoff_zipcode][month] += 1

# Load in New York data
nyc_data = pd.read_csv("C:\\Users\\CodeB\\Documents\\GitHub\\transportation-transformation\\data\\new_york\\2019_Yellow_Taxi_Trip_Data_latlon.csv")
nyc_df = pd.DataFrame(nyc_data)
# keep only relevant columns
nyc_df = nyc_df[["tpep_pickup_datetime", "PUlatitude", "PUlongitude", "DOlatitude", "DOlongitude"]]
# drop NAs in relevant fields
nyc_df = nyc_df.dropna(subset=["PUlatitude", "PUlongitude", "DOlatitude", "DOlongitude", "tpep_pickup_datetime"])
# get month from datetime
months = []
for time in nyc_df["tpep_pickup_datetime"]:
    months.append(time.split("/")[0])
nyc_df["month"] = months
nyc_df = nyc_df.drop(["tpep_pickup_datetime"], axis=1)

for index, row in nyc_df.iterrows():
    print(index)
    insert_trip(row)

with open("pickup_zipcode_to_month_freq.json", "w") as fout:
    json.dump(pickup_zipcode_to_month_freq, fout)

with open("dropoff_zipcode_to_month_freq.json", "w") as fout:
    json.dump(dropoff_zipcode_to_month_freq, fout)
