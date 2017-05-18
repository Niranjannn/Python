import datetime
import numpy as np
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
import pandas as pd

data = pd.read_excel('data.xlsx')
print data.describe

android_data_X = data[['datetime','Android_Average_rating','Android_File_size','Android_Rating_4','Android_Rating_5','Android_Rating_2','Android_Rating_3','Android_Rating_1']]


android_data_Y = data[['Android_Total_rating']]

#creating test and train set with sklearn cross validatoon -train_test_split() method
X_train,X_test,y_train,y_test = train_test_split(android_data_X,android_data_Y,random_state=1)
# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train, y_train)

yfit=regr.predict(X_test)
# The coefficients

print('Coefficients: \n', regr.coef_)
print("intercept", regr.intercept_)
# The mean squared error
print("root Mean squared error: %.2f"
          % (np.mean((regr.predict(X_test) - y_test) ** 2))**0.5)
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(X_test, y_test))

#converting the datetime to be tested in to nanoseconds
epoch = datetime.datetime.utcfromtimestamp(0)
def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0
year=2016
month=11
day=01
hour=23
Min=50
sec=00

dateTime=datetime.datetime(year,month,day,hour,Min,sec)
date= unix_time_millis(dateTime)

B0= regr.intercept_[0]
B1=regr.coef_[0][0]
B2=regr.coef_[0][1]
B3=regr.coef_[0][2]
B4=regr.coef_[0][3]
B5=regr.coef_[0][4]
B6=regr.coef_[0][5]
B7=regr.coef_[0][6]
B8=regr.coef_[0][6]
B8=regr.coef_[0][7]

print B0,B1,B2,B3,B4,B5,B6,B7,B8

#predicting the android_all_rating based on date_time including all independent variables for the linear equation.
y=B0+(B1*date)
print("android predicted value for Android_Total_rating :",y)
