import datetime
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.cross_validation import train_test_split
import pandas as pd


data = pd.read_excel('data.xlsx')
print data.describe

data_X = data[['datetime','ios_File_size','ios_current_rating']]
data_Y = data[['ios_all_rating']]

#creating test and train set with sklearn cross validatoon -train_test_split() method
X_train,X_test,y_train,y_test = train_test_split(data_X,data_Y,random_state=1)

# Create linear regression object
model = Ridge(alpha = .5)
model.fit(X_train,y_train)

print('Coefficients: \n', model.coef_)
print("intercept", model.intercept_)
# The mean squared error
print("root Mean squared error: %.2f"
          % (np.mean((model.predict(X_test) - y_test) ** 2))**0.5)
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % model.score(X_test, y_test))


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

B0= model.intercept_[0]
B1=model.coef_[0][0]
B2=model.coef_[0][1]
B3=model.coef_[0][2]
print B0,B1,B2,B3


#predicting the android_all_rating based on date_time including all independent variable.
y=B0+(B1*date)
print("ios predicted value for ios_all_rating :",y)
