import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import folium as folium
import json

df = pd.read_csv("/Users/Stephanie/Desktop/transportation-transformation-master/data/chicago/chicago_cta_combined_dropoff.csv")
df = df[["zipcode","income","population","month_total"]]
df['zipcode'] = df['zipcode'].astype('str')
df = df.drop_duplicates()
df["population"] = df["population"].apply(lambda x: x.replace(",","")).astype(int)
df["month_total"] = df["month_total"].apply(lambda x: x.replace(",","")).astype(int)

with open('/Users/Stephanie/Desktop/transportation-transformation-master/data/chicago/Boundaries - ZIP Codes.geojson','r') as chicago_geo:
    geo_data = json.load(chicago_geo)
temp = geo_data

#removes all zipcodes that are not in our train dropoff dataset
geo_zip = []
for i in range(len(temp['features'])):
    if temp['features'][i]['properties']['zip'] in list(df['zipcode'].unique()):
        geo_zip.append(temp['features'][i])

new_json = dict.fromkeys(['type','features'])
new_json['type'] = 'FeatureCollection'
new_json['features'] = geo_zip

open("cleaned_geodata.json", "w").write(json.dumps(new_json, sort_keys=True, indent=4, separators=(',', ': ')))

def map_feature_by_zipcode(zipcode_data, col):
    """
    Generates a folium map of Chicago
    :param zipcode_data: zipcode dataset
    :param col: feature to display
    :return: m
    """

    # read updated geo data
    
    king_geo = "cleaned_geodata.json"

    # Initialize Folium Map with Chicago latitude and longitude
    m = folium.Map(location=[41.88, -87.63], zoom_start=9,
                   detect_retina=True, control_scale=False)

    # Create choropleth map
    folium.Choropleth(
        geo_data=king_geo,
        data=zipcode_data,
        #geo_data = temp,
        name='choropleth',
        # col: feature of interest
        columns=['zipcode', col],
        key_on='feature.properties.zip',
        fill_color='GnBu',
        fill_opacity=0.65,
        line_opacity=0.3,
        legend_name='average zip code ' + col,
        line_color = 'black',
        line_weight = 2
    ).add_to(m)

    folium.LayerControl().add_to(m)

    # Save map based on feature of interest
    m.save("chicago_train_" + col + '.html')

    return m

map_feature_by_zipcode(df, 'month_total')


# FOLIUM INFO SOURCE: https://medium.com/@sosterburg/mapping-data-with-folium-356f0d6f88a9