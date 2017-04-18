# Yelp Data Homework 

First we have to import the file into python. 

```
path = './data/' 
url = path + 'yelp.csv'
yelp = pd.read_csv(url, parse_dates=True)
```