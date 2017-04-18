import pandas as pd 
import matplotlib as plt
from sklearn import metrics

#Task 1: Read yelp.csv into a data frame

path = './data/' 
url = path + 'yelp.csv'
yelp = pd.read_csv(url, parse_dates=True) #index_col='stars'

#Task 2: Explore the relationship between each of the vote types (cool/useful/funny) and the number of stars

print yelp.groupby('stars').mean()

import seaborn as sns
sns.heatmap(yelp.corr())

#yelp.plot(kind='scatter', x='cool', y='stars', alpha=0.2)
sns.lmplot(x='cool', y='stars', data=yelp, aspect=0.5, scatter_kws={'alpha':0.2})
sns.lmplot(x='useful', y='stars', data=yelp, aspect=0.5, scatter_kws={'alpha':0.2})
sns.lmplot(x='funny', y='stars', data=yelp, aspect=0.5, scatter_kws={'alpha':0.2})

#Task 3: Define cool/useful/funny as the feature matrix X, and stars as the response vector y

feature_cols = ['cool', 'useful', 'funny']
X = yelp[feature_cols]
y = yelp.stars

#Task 4: Fit a linear regression model

from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X, y)
print linreg.intercept_
print linreg.coef_
zip(feature_cols, linreg.coef_)


#Task 5: Valuate the model by splitting it into training and testing sets and computing the RMSE. Does the RMSE make intuitive sense to you?

from sklearn.cross_validation import train_test_split
import numpy as np

def train_test_rmse(fc):
    X = yelp[fc]
    y = yelp.stars
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    linreg2 = LinearRegression()
    linreg2.fit(X_train, y_train)
    y_pred = linreg2.predict(X_test)
    return np.sqrt(metrics.mean_squared_error(y_test, y_pred))

print train_test_rmse(['cool', 'useful', 'funny'])

#Task 6: Try removing some of the features and see if the RMSE improves

print train_test_rmse(['useful'])
print train_test_rmse(['funny'])
print train_test_rmse(['cool'])
print train_test_rmse(['cool', 'useful'])
print train_test_rmse(['cool', 'funny'])
print train_test_rmse(['useful', 'funny'])





