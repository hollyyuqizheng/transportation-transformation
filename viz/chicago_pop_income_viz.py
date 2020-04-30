import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

drop_df = pd.read_csv("/Users/Stephanie/Desktop/transportation-transformation-master/data/chicago/chicago_cta_combined_dropoff.csv")
pick_df = pd.read_csv("/Users/Stephanie/Desktop/transportation-transformation-master/data/chicago/chicago_cta_combined_pickup.csv")
#print(drop_df)
df = drop_df[["zipcode","population","income"]]
df = df.drop_duplicates()

df["population"] = df["population"].apply(lambda x: x.replace(",","")).astype(int)
population = df["population"]
income = df["income"]
zipcode = df["zipcode"]
df.sort_values("zipcode",ascending=True,inplace=True)

df.plot(x="zipcode",y="population",kind="bar")
plt.grid(b=bool,which = 'both',axis='both', alpha=0.75)
plt.xlabel('Zip Code',fontsize=15)
plt.ylabel('Population',fontsize=15)
#plt.xticks(np.arange(min(zipcode)-1,max(zipcode)+1,step = 10),zipcode,fontsize=10)
plt.yticks(np.arange(10000, 120000, 10000),fontsize=5)
plt.title('Chicago Population per Zip Code',fontsize=15)
plt.show()

df.plot(x="zipcode",y="income",kind="bar")
plt.grid(b=bool,which = 'both',axis='both', alpha=0.75)
plt.xlabel('Zip Code',fontsize=15)
plt.ylabel('Income',fontsize=15)
#plt.xticks(np.arange(min(zipcode)-1,max(zipcode)+1,step = 10),zipcode,fontsize=10)
plt.yticks(np.arange(10000, 90000, 5000),fontsize=5)
plt.title('Chicago Income per Zip Code',fontsize=15)
plt.show()

