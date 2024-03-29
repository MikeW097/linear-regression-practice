import pandas as pd
from sklearn.linear_model import LinearRegression

#read data
houseprice = pd.read_csv('housing.data', sep=' ', header=None)
print(houseprice.head())
'''
x_values = houseprice.iloc[[0:13]]
y_values = houseprice.iloc[[13]]

#train model
HousePrice = LinearRegression()
HousePrice.fit(x_values, y_values)

#predict
sample_house = [[2.29690000e-01, 0.00000000e+00, 1.05900000e+01, 0.00000000e+00, 4.89000000e-01,
                6.32600000e+00, 5.25000000e+01, 4.35490000e+00, 4.00000000e+00, 2.77000000e+02,
                1.86000000e+01, 3.94870000e+02, 1.09700000e+01]]
print(HousePrice.predict(sample_house))
'''
