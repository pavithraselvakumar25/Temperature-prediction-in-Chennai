import pandas as pd
import numpy as np

data = pd.read_csv("data/Temperature Data.csv")

data =data.drop("Years",axis =1)

x = np.array(data.columns,dtype=int)
x = x.reshape(len(x),1)

frm = input("Enter the time period in MM-YYYY: ")
month = int(frm[0:2])
year = int(frm[3:])

y = data.loc[month-1].values
y = y.reshape(len(y),1)

