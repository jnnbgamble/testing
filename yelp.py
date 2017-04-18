import pandas as pd 
import matplotlib as plt
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import numpy as np

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





#linreg.fit(X['cool'], y)



