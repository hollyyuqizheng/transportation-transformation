#!/usr/bin/env python3

from google.cloud import bigquery
import pandas as pd

client = bigquery.Client()

ch_dataset_ref = client.dataset("chicago_taxi_trips", project="bigquery-public-data")
ch_dset = client.get_dataset(ch_dataset_ref)
print([x.table_id for x in client.list_tables(ch_dset)])
ch_taxi = client.get_table(ch_dset.table("taxi_trips"))

### For exporting to GCP
# ch_taxi_ref = ch_dataset_ref.table("taxi_trips")
#
# destination_uri = "C:\\Users\\CodeB\\Documents\\GitHub\\transportation-transformation\\data\\chicago\\chicago_taxi_kaggle.csv"
#
# extract_job = client.extract_table(
#     ch_taxi_ref,
#     destination_uri
# )
# extract_job.result()

schema = ch_taxi.schema
print(schema)
