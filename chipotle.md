# Chipotle Data Homework 

First we have to import the file into python. 

```
import pandas as pd
path = 'data/chipotle.tsv'

chipotle = pd.DataFrame.from_csv(path, sep='\t')
```

1. Look at the head and the tail of chipotle.tsv in the data subdirectory of this repo. Think for a minute about how the data is structured. What do you think each column means? What do you think each row means? Tell me! (If you're unsure, look at more of the file contents.)

```
print chipotle.tail()
```

1833	1	Steak Burrito	[Fresh Tomato Salsa, [Rice, Black Beans, Sour Cream, Cheese, Lettuce, Guacamole]]	$11.75 
1833	1	Steak Burrito	[Fresh Tomato Salsa, [Rice, Sour Cream, Cheese, Lettuce, Guacamole]]	$11.75 
1834	1	Chicken Salad Bowl	[Fresh Tomato Salsa, [Fajita Vegetables, Pinto Beans, Guacamole, Lettuce]]	$11.25 
1834	1	Chicken Salad Bowl	[Fresh Tomato Salsa, [Fajita Vegetables, Lettuce]]	$8.75 
1834	1	Chicken Salad Bowl	[Fresh Tomato Salsa, [Fajita Vegetables, Pinto Beans, Lettuce]]	$8.75 