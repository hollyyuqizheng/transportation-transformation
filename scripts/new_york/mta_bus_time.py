#!/usr/bin/env python3

import pandas as pd
import pickle

data = pd.read_csv("../../data/new_york/MTA-Bus-Time_2014-08-01.txt", sep="\t")
df = pd.DataFrame(data)
print(df.describe)
