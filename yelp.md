# Yelp Data Homework 

First we have to import the file into python as well as pandas. CSV is in the data subdirectory. 

```
import pandas as pd
path = './data/' 
url = path + 'yelp.csv'
```

**1 Read yelp.csv into a data frame**

```
yelp = pd.read_csv(url, parse_dates=True)
```

**2 Explore the relationship between each of the vote types (cool/useful/funny) and the number of stars.**
   
Let's take a look at what the mean number of cool/useful/funny ratings look like by star count: 
                                                            
```
print yelp.groupby('stars').mean()
```                                                
                                       
Now let's look at the heat map of the correlations of the data. 

```
import seaborn as sns
sns.heatmap(yelp.corr())
```

Now let's graph stars against all the values in our feature matrix.

```
sns.lmplot(x='cool', y='stars', data=yelp, aspect=0.5, scatter_kws={'alpha':0.2})
sns.lmplot(x='useful', y='stars', data=yelp, aspect=0.5, scatter_kws={'alpha':0.2})
sns.lmplot(x='funny', y='stars', data=yelp, aspect=0.5, scatter_kws={'alpha':0.2})
```

Interestingly enough the "useful" and "funny" traits tend to be inversely correlated with the number of stars recieved. This makes sense when you consider user behavior on yelp; users often leave funny comments on restaurants or businesses they rate 1 star, and a 1 star rating could turn out to be very useful. 

                     
**3 Define cool/useful/funny as the feature matrix X, and stars as the response vector y.**

```
feature_cols = ['cool', 'useful', 'funny']
X = yelp[feature_cols]
y = yelp.stars
```

**4 Fit a linear regression model and interpret the coefficients. Do the coefficients make intuitive sense to you? Explore the Yelp website to see if you detect similar trends.**

```
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X, y)
print linreg.intercept_
print linreg.coef_
zip(feature_cols, linreg.coef_)
```

The coefficients do make sense. As mentioned earlier, it makes a lot of sense that "useful" and "funny" categories would be inversely proportional to the number of stars given. 

**5 Valuate the model by splitting it into training and testing sets and computing the RMSE. Does the RMSE make intuitive sense to you?**

```
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
```

Define a function that splits the original data into test and training chunks and returns the RMSE. As the data is randomly divided up, the RSME is never the exact same. But it remains around 1.15 - 1.22.

**6 Try removing some of the features and see if the RMSE improves.**

```
print train_test_rmse(['useful'])
print train_test_rmse(['funny'])
print train_test_rmse(['cool'])
print train_test_rmse(['cool', 'useful'])
print train_test_rmse(['cool', 'funny'])
print train_test_rmse(['useful', 'funny'])
```

The RMSE is occasionally better with some of these reductions. 