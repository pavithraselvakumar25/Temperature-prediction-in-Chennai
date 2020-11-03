# TEMPERATURE PREDICTION IN CHENNAI

# IMPORTING REQUIRED MODULES
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

# GETTING TIME PERIOD STRING FROM THE USER
frm = input("Enter the time period in MM-YYYY: ")
month = int(frm[0:2])
year = int(frm[3:])

# DATA SEGMENTATION
data = pd.read_csv("data/Temperature Data.csv")


x = np.array(data.columns,dtype=int)
x = x.reshape(len(x),1)

y = data.loc[month-1].values
y = y.reshape(len(y),1)


#LINEAR REGRESSION
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)

#PRINTING VALUES OF INTERCEPT AND SLOPE BEFORE RESHAPING
print("Values of intercept and slope are {} and {} respectively(before reshaping)".format(model.intercept_,model.coef_))

#PREDICTION
y_pred = model.predict(x)

#PLOTTING THE VALUES USING MATPLOTLIB
plt.scatter(x,y,color = "red")
plt.plot(x,model.predict(x),color="green")
plt.title("Temperature prediction in Chennai")
plt.xlabel("Years")
plt.ylabel("Temperature(in Fahrenheit)")
plt.show()

#POLYNOMIAL REGRESSION
poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(x)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly,y)

#PREDICTION
lin_reg_2.predict(poly_reg.fit_transform([[x]])

#PLOTTING THE VALUES USING MATLAB
plt.scatter(x,y,color = 'red')
plt.plot(x,lin_reg_2.predict(poly_reg.fit_tranform(x)),color = 'blue')
plt.title('Temperature prediction in Chennai')
plt.xlabel('Years')
plt.ylabel('Temperature(in Fehrenheit)')
plt.show()
