import pandas as pd
import numpy as np

path = '../data/work/population2011.csv'
df = pd.read_csv(path,sep=',')
listOfName = []
print(df.shape[0])
for i in range(df.shape[0]):
    if df.iloc[i].AreaName != "INDIA":
        temp = df.iloc[i].AreaName[7:-1].lower()
        df.iloc[i].AreaName = temp
        print(df.iloc[i].AreaName)

df.to_csv(path,index=False)