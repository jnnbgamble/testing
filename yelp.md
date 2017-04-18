# Yelp Data Homework 

First we have to import the file into python. CSV is in the data subdirectory. 

```
path = './data/' 
url = path + 'yelp.csv'
```

**1 Read yelp.csv into a data frame**

```
yelp = pd.read_csv(url, parse_dates=True)
```

**2 Explore the relationship between each of the vote types (cool/useful/funny) and the number of stars.**
                                                            
**3 Define cool/useful/funny as the feature matrix X, and stars as the response vector y.**

**4 Fit a linear regression model and interpret the coefficients. Do the coefficients make intuitive sense to you? Explore the Yelp website to see if you detect similar trends.**

**5 Valuate the model by splitting it into training and testing sets and computing the RMSE. Does the RMSE make intuitive sense to you?**

**6 Try removing some of the features and see if the RMSE improves.**

**7 BONUS: Think of some new features you could create from the existing data that might be predictive of the response. Figure out how to create those features in Pandas, add them to your model, and see if the RMSE improves.**

**8 Compare your best RMSE on the testing set with the RMSE for the "null model", which is the model that ignores all features and simply predicts the mean response value in the testing set.**