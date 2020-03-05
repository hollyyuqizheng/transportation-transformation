import pandas as pd
import requests

data = pd.read_csv("C:\\Users\\CodeB\\Documents\\GitHub\\transportation-transformation\\data\\new_york\\uber-tlc-foil-response\\uber-trip-data\\taxi-zone-lookup.csv")
df = pd.DataFrame(data)

overpass_url = "http://overpass-api.de/api/interpreter"
nominatim_url = "https://nominatim.openstreetmap.org/search"

# r = requests.get(nominatim_url + "?q=newark+airport+new+york&format=json")
# if r.status_code == 200:
#     data = r.json()
#     print(data)

lons = []
lats = []
def get_latlon(zone):
    zone = zone.split("/")[0]
    print(zone)
    url = nominatim_url + "?q=" + zone.lower() + "+new+york&format=json"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        if len(data) > 0:
            coords = data[0].get("boundingbox")
            print("coords: ", coords)
            if coords != None:
                lat = (float(coords[0]) + float(coords[1])) / 2
                lats.append(lat)
                lon = (float(coords[2]) + float(coords[3])) / 2
                lons.append(lon)
        else:
            print("No data")
    else:
        print(r.status_code)
for index, row in df.iterrows():
    print("index: ", index)
    zone = row["Zone"]
    get_latlon(zone)

longitude = pd.DataFrame(lons)
latitude = pd.DataFrame(lats)

clean_df = pd.concat([df, longitude, latitude], axis=1)
print(clean_df.head)

clean_df.to_csv("C:\\Users\\CodeB\\Documents\\GitHub\\transportation-transformation\\data\\new_york\\uber-tlc-foil-response\\uber-trip-data\\taxi-latlon-lookup-2.csv")
