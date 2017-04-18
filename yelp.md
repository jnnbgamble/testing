# Yelp Data Homework 

First we have to import the file into python as well as all of our libraries. CSV is in the data subdirectory. 

```
import pandas as pd
import seaborn as sns
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

**5 Valuate the model by splitting it into training and testing sets and computing the RMSE. Does the RMSE make intuitive sense to you?**

**6 Try removing some of the features and see if the RMSE improves.**

**7 BONUS: Think of some new features you could create from the existing data that might be predictive of the response. Figure out how to create those features in Pandas, add them to your model, and see if the RMSE improves.**

**8 BONUS: Compare your best RMSE on the testing set with the RMSE for the "null model", which is the model that ignores all features and simply predicts the mean response value in the testing set.**