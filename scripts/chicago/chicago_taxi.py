#!/usr/bin/env python3

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
#client = Socrata("data.cityofchicago.org", None)

# Example authenticated client (needed for non-public datasets):
client = Socrata("data.cityofchicago.org",
                None)

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
# results = client.get("wrvz-psew", limit=2000)
results = client.get("wrvz-psew", where="trip_start_timestamp between '2019-01-01T00:00:00' and '2019-01-31T23:59:59'")

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
results_df.to_csv("C:\\Users\\CodeB\\Documents\\GitHub\\transportation-transformation\\data\\chicago\\chicago_taxi_2019_01_v1.csv")
print(results_df.describe)
