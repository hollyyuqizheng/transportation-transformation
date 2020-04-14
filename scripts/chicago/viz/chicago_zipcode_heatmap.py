import pandas as pd
import re
from datetime import datetime
from dateutil.parser import parse
import missingno as msno
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import json
import folium

data = pd.read_csv("C:\\Users\\CodeB\\Documents\\GitHub\\transportation-transformation\\data\\chicago\\chicago_zipcode_combined_dropoff_2010.tsv", sep="\t")
df = pd.DataFrame(data)

def create_map(table, zips, mapped_feature, add_text = ''):
    # reading of the updated GeoJSON file
    chi_geo = r'chicago_zip_codes.geojson'
    # initiating a Folium map with LA's longitude and latitude
    m = folium.Map(location = [41.8781, 87.6298], zoom_start = 11)
    # creating a choropleth map
    m.choropleth(
        geo_data = chi_geo,
        fill_opacity = 0.7,
        line_opacity = 0.2,
        data = table,
        # refers to which key within the GeoJSON to map the ZIP code to
        key_on = 'feature.properties.zip',
        # first element contains location information, second element contains feature of interest
        columns = [zips, mapped_feature],
        fill_color = 'RdYlGn',
        legend_name = (' ').join(mapped_feature.split('_')).title() + ' ' + add_text + ' Across Chicago'
    )
    folium.LayerControl().add_to(m)
    # save map with filename based on the feature of interest
    m.save(outfile = mapped_feature + '_map.html')