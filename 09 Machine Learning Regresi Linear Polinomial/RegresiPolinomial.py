from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import numpy as np

x = [[0], [4], [8], [12], [16], [20], [24], [28], [32], [36]]
y = [0, 3, 8, 15, 24, 35, 48, 63, 80, 99]

predict = np.array ([[12]])
poly = PolynomialFeatures(degree=2)
x_ = poly.fit_transform(x)
predict_ = poly.fit_transform(predict)
regr = linear_model.LinearRegression()
regr.fit (x_,y)

print ("Prediksi")
print ("Input = ", predict)
print ("Output = ", regr.predict(predict_))
