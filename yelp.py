import pandas as pd 
import matplotlib as plt
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import numpy as np

#Task 1

path = './data/' 
url = path + 'yelp.csv'
yelp = pd.read_csv(url, parse_dates=True) #index_col='stars'

#Task 2

print yelp.groupby('stars').mean()

import seaborn as sns
sns.heatmap(yelp.corr())

#yelp.plot(kind='scatter', x='cool', y='stars', alpha=0.2)
sns.lmplot(x='stars', y='cool', data=yelp, aspect=0.5, scatter_kws={'alpha':0.2})
sns.lmplot(x='stars', y='useful', data=yelp, aspect=0.5, scatter_kws={'alpha':0.2})
sns.lmplot(x='stars', y='funny', data=yelp, aspect=0.5, scatter_kws={'alpha':0.2})

#Task 3

feature_cols = ['cool', 'useful', 'funny']
X = yelp[feature_cols]
y = yelp.stars
print y

#Treat as categorical variable, look for differences in groups
#mean of cool/funny/useful for each star rating 



#Display correlation matrix of the vote types 
#Display multiple scatter plots 



#cool/funny/useful is feature matrix, stars is response vector y



#fit linear regression model and interpret coefficients 



#Evaluate model by fitting RMSE



#Remove features and see if RSME improves 