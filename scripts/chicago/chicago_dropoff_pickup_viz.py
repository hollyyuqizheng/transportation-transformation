import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

drop_df = pd.read_csv("/Users/Stephanie/Desktop/transportation-transformation-master/data/chicago/chicago_cta_combined_dropoff.csv")
pick_df = pd.read_csv("/Users/Stephanie/Desktop/transportation-transformation-master/data/chicago/chicago_cta_combined_pickup.csv")

df2 = drop_df[["month_total","zipcode"]]
df2["month_total"] = df2["month_total"].apply(lambda x: x.replace(",","")).astype(int)
df2 = df2.groupby("zipcode").mean()
print(df2)
print(list(df2.columns))
month_total = df2["month_total"]

df2.plot(y='month_total',kind='bar')
plt.grid(b=bool,which = 'both',axis='both', alpha=0.75)
plt.xlabel('Zip Code',fontsize=15)
plt.ylabel('Average Monthly Train Dropoff',fontsize=15)
#plt.xticks(np.arange(min(zipcode)-1,max(zipcode)+1,step = 10),zipcode,fontsize=10)
plt.yticks(np.arange(20000, 320000, 25000),fontsize=5)
plt.title('Chicago Average Monthly Train Dropoff per Zip Code',fontsize=15)
plt.show()



df3 = pick_df[["month_total","zipcode"]]
print(df3["month_total"])
df3["month_total"] = df3["month_total"].apply(lambda x: x.replace(",","")).astype(int)
df3 = df3.groupby("zipcode").mean()
month_total = df3["month_total"]

df3.plot(y='month_total',kind='bar')
plt.grid(b=bool,which = 'both',axis='both', alpha=0.75)
plt.xlabel('Zip Code',fontsize=15)
plt.ylabel('Average Monthly Train Pickup',fontsize=15)
#plt.xticks(np.arange(min(zipcode)-1,max(zipcode)+1,step = 10),zipcode,fontsize=10)
plt.yticks(np.arange(20000, 320000, 25000),fontsize=5)
plt.title('Chicago Average Monthly Train Pickup per Zip Code',fontsize=15)
plt.show()