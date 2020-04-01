#!/usr/bin/env python3

# Get Chicago data per day
import pandas as pd
from sodapy import Socrata
import math
import json

# Load Chicago zipcode data
zipcode_data = pd.read_csv("C:\\Users\\CodeB\\Documents\\GitHub\\transportation-transformation\\data\\chicago\\Chicago_Pop_ZipCode.csv")
zipcode_df = pd.DataFrame(zipcode_data)
# Dropping unnamed columns at end
zipcode_df = zipcode_df.iloc[:, 1:4]

# Split latlon column into two
lats = []
lons = []
for pair in zipcode_df["Long, Lat"]:
    lat_lon = pair.split(",")
    lats.append(float(lat_lon[0]))
    lons.append(float(lat_lon[1]))
zipcode_df["lat"] = lats
zipcode_df["lon"] = lons

# Dictionary of community areas to zipcode
ca_to_zipcode = {}
with open("C:\\Users\\CodeB\\Documents\\GitHub\\transportation-transformation\\data\\chicago\\taxi_new\\community_area_to_zipcode.json", "r") as fin:
    ca_to_zipcode = json.load(fin)

def get_zipcode(lat, lon, ca):
    """
    Given a latitude and longitude, find the closest zipcode.

    Distance is not the real-world distance, but Euclidean distance of lat-lon coordinates.
    """
    if ca_to_zipcode.get(ca) == None:
        min_zip = None
        min_dist = float("inf")
        for idx, row in zipcode_df.iterrows():
            dist = math.sqrt((row["lat"] - float(lat)) ** 2 + (row["lon"] - float(lon)) ** 2)
            if dist < min_dist:
                min_zip = row["Zip Code"]
                min_dist = dist

        ca_to_zipcode[ca] = min_zip
        with open("community_area_to_zipcode.json", "w") as fout:
            json.dump(ca_to_zipcode, fout)

        return min_zip
    else:
        return ca_to_zipcode[ca]


# Dictionary of zipcode to dictionary of month to frequency
# For example: {60601: {1: 50, 2: 25, ...}, ...}
pickup_zipcode_to_month_freq = {}
# with open("pickup_zipcode_to_month_freq.json", "r") as fin:
#     pickup_zipcode_to_month_freq = json.load(fin)

# for zc in pickup_zipcode_to_month_freq.keys():
#     pickup_zipcode_to_month_freq[zc]["5"] = 0

dropoff_zipcode_to_month_freq = {}
# with open("dropoff_zipcode_to_month_freq.json", "r") as fin:
#     dropoff_zipcode_to_month_freq = json.load(fin)
#
# for zc in dropoff_zipcode_to_month_freq.keys():
#     dropoff_zipcode_to_month_freq[zc]["5"] = 0

def insert_day(df, month):
    """
    Take a df of taxi records for a single day and inserts it into zipcode_to_month_freq.
    """
    df = df.dropna(subset=["pickup_centroid_latitude", "pickup_centroid_longitude", "pickup_community_area", "dropoff_centroid_latitude", "dropoff_centroid_longitude", "dropoff_community_area"])

    for idx, row in df.iterrows():
        pickup_zipcode = get_zipcode(row["pickup_centroid_latitude"], row["pickup_centroid_longitude"], row["pickup_community_area"])
        dropoff_zipcode = get_zipcode(row["dropoff_centroid_latitude"], row["dropoff_centroid_longitude"], row["dropoff_community_area"])

        if pickup_zipcode_to_month_freq.get(pickup_zipcode) == None:
            pickup_zipcode_to_month_freq[pickup_zipcode] = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
        pickup_zipcode_to_month_freq[pickup_zipcode][month] += 1

        if dropoff_zipcode_to_month_freq.get(dropoff_zipcode) == None:
            dropoff_zipcode_to_month_freq[dropoff_zipcode] = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
        dropoff_zipcode_to_month_freq[dropoff_zipcode][month] += 1

    with open("pickup_zipcode_to_month_freq.json", "w") as fout:
        json.dump(pickup_zipcode_to_month_freq, fout)

    with open("dropoff_zipcode_to_month_freq.json", "w") as fout:
        json.dump(dropoff_zipcode_to_month_freq, fout)

# # Example authenticated client (needed for non-public datasets):
client = Socrata("data.cityofchicago.org",
                None)

# Get taxi data per day in 2019
for month in range(1, 13):
    month_str = str(month)
    if len(month_str) == 1:
        month_str = "0" + month_str

    if month in [1,3,5,7,8,10,12]:
        # 31 days
        for day in range(1, 32):
            day_str = str(day)
            if len(day_str) == 1:
                day_str = "0" + day_str

            # Requesting taxi ride data for that date
            time_query = "trip_start_timestamp between '2019-" + month_str + "-" + day_str + "T00:00:00' and '2019-" + month_str + "-" + day_str + "T23:59:59'"
            print(time_query)
            results = client.get("wrvz-psew", where=time_query, limit=100000)
            results_df = pd.DataFrame.from_records(results)
            insert_day(results_df, month)
    elif month == 2:
        # 28 days in 2019
        for day in range(1, 29):
            day_str = str(day)
            if len(day_str) == 1:
                day_str = "0" + day_str

            time_query = "trip_start_timestamp between '2019-" + month_str + "-" + day_str + "T00:00:00' and '2019-" + month_str + "-" + day_str + "T23:59:59'"
            print(time_query)
            results = client.get("wrvz-psew", where=time_query, limit=100000)
            results_df = pd.DataFrame.from_records(results)
            insert_day(results_df, month)
    else:
        # 30 days
        for day in range(1, 31):
            day_str = str(day)
            if len(day_str) == 1:
                day_str = "0" + day_str

            time_query = "trip_start_timestamp between '2019-" + month_str + "-" + day_str + "T00:00:00' and '2019-" + month_str + "-" + day_str + "T23:59:59'"
            print(time_query)
            results = client.get("wrvz-psew", where=time_query, limit=100000)
            results_df = pd.DataFrame.from_records(results)
            insert_day(results_df, month)
