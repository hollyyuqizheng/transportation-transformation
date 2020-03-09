import shapefile
import pandas as pd

# # TODO: wrong filepath
# data = pd.read_csv("C:\\Users\\CodeB\\Documents\\GitHub\\transportation-transformation\\data\\new_york\\uber-tlc-foil-response\\uber-trip-data\\taxi-zone-lookup.csv")
# df = pd.DataFrame(data)

def get_lat_lon(sf):
    content = []
    for sr in sf.shapeRecords():
        shape = sr.shape
        rec = sr.record
        loc_id = rec[shp_dic['locationid']]

        x = (shape.bbox[0]+shape.bbox[2])/2
        y = (shape.bbox[1]+shape.bbox[3])/2

        content.append((loc_id, x, y))
    return pd.DataFrame(content, columns=["LocationID", "longitude", "latitude"])


# Script is from https://chih-ling-hsu.github.io/2018/05/14/NYC
sf = shapefile.Reader("C:\\Users\\CodeB\\Documents\\GitHub\\transportation-transformation\\data\\new_york\\nyu-2451-36743-shapefile\\nyu_2451_36743.shp")
fields_name = [field[0] for field in sf.fields[1:]]
shp_dic = dict(zip(fields_name, list(range(len(fields_name)))))
attributes = sf.records()
shp_attr = [dict(zip(fields_name, attr)) for attr in attributes]

df_loc = pd.DataFrame(shp_attr).join(get_lat_lon(sf).set_index("LocationID"), on="locationid")
df_loc.to_csv("Taxi_Zone_latlon.csv")
print(df_loc.head())
print(list(df_loc.columns.values))

df_pu_loc = df_loc.rename(columns={"locationid": "PULocationID", "latitude": "PUlatitude", "longitude":"PUlongitude"})
print(df_pu_loc.head())
print(list(df_pu_loc.columns.values))
df_pu_loc = df_pu_loc[["PULocationID", "PUlatitude", "PUlongitude"]]
df_do_loc = df_loc.rename(columns={"locationid": "DOLocationID", "latitude": "DOlatitude", "longitude":"DOlongitude"})
df_do_loc = df_do_loc[["DOLocationID", "DOlatitude", "DOlongitude"]]

# Merge with Yellow Taxi data
data = pd.read_csv("C:\\Users\\CodeB\\Documents\\GitHub\\transportation-transformation\\data\\new_york\\2019_Yellow_Taxi_Trip_Data.csv")
df = pd.DataFrame(data)

merged = df.set_index("PULocationID").join(df_pu_loc.set_index("PULocationID"))
merged_final = merged.set_index("DOLocationID").join(df_do_loc.set_index("DOLocationID"))
print(list(merged_final.columns.values))

merged_final.to_csv("2019_Yellow_Taxi_Trip_Data_latlon.csv")
