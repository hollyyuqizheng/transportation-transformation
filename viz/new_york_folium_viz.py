import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import folium as folium
import json

df = pd.read_csv("/Users/Stephanie/Desktop/transportation-transformation-master/data/new_york/ny_zipcode_combined_dropoff_w_index.csv")
df = df[["zipcode","avg_household_income (thousand)","population (thousand)","subway_total (billion)","taxi_total (million)"]]
df['zipcode'] = df['zipcode'].astype('str')
df = df.drop_duplicates()
df["population (thousand)"] = df["population (thousand)"].apply(lambda x: x*1000).astype(int)
df["subway_total (billion)"] = df["subway_total (billion)"].apply(lambda x: x*1000000000).astype(int)
df["taxi_total (million)"] = df["taxi_total (million)"].apply(lambda x: x*1000000).astype(int)
df["avg_household_income (thousand)"] = df["avg_household_income (thousand)"].apply(lambda x: x*1000).astype(int)

with open('/Users/Stephanie/Desktop/transportation-transformation-master/data/new_york/nyc_zip_code_polygons.geojson','r') as nyc_geo:
    geo_data = json.load(nyc_geo)
temp = geo_data

#removes all zipcodes that are not in our train dropoff dataset
geo_zip = []
for i in range(len(temp['features'])):
    if temp['features'][i]['properties']['postalcode'] in list(df['zipcode'].unique()):
        geo_zip.append(temp['features'][i])

new_json = dict.fromkeys(['type','features'])
new_json['type'] = 'FeatureCollection'
new_json['features'] = geo_zip

open("cleaned_geodata.json", "w").write(json.dumps(new_json, sort_keys=True, indent=4, separators=(',', ': ')))

def map_feature_by_zipcode(zipcode_data, col):
    """
    Generates a folium map of New York
    :param zipcode_data: zipcode dataset
    :param col: feature to display
    :return: m
    """

    # read updated geo data
    
    king_geo = "cleaned_geodata.json"

    # Initialize Folium Map with New York latitude and longitude
    m = folium.Map(location=[40.71,-74.00], zoom_start=9,
                   detect_retina=True, control_scale=False)

    # Create choropleth map
    folium.Choropleth(
        geo_data=king_geo,
        data=zipcode_data,
        #geo_data = temp,
        name='choropleth',
        # col: feature of interest
        columns=['zipcode', col],
        key_on='feature.properties.postalcode',
        fill_color='GnBu',
        #fill_color='Greens',
        fill_opacity=0.65,
        line_opacity=0.3,
        legend_name='average zip code ' + col,
        line_color = 'black',
        line_weight = 2
    ).add_to(m)

    folium.LayerControl().add_to(m)

    # Save map based on feature of interest
    m.save("new york_dropoff_" + col + '.html')

    return m

map_feature_by_zipcode(df, 'taxi_total (million)')


# FOLIUM INFO SOURCE: https://medium.com/@sosterburg/mapping-data-with-folium-356f0d6f88a9