# Chipotle Data Homework 

First we have to import the file into python. I have chipotle.tsv saved in a subdirectory called data.

```
import pandas as pd
path = 'data/chipotle.tsv'

chipotle = pd.read_csv(path, sep='\t')
```

**1 Look at the head and the tail of chipotle.tsv in the data subdirectory of this repo. Think for a minute about how the data is structured. What do you think each column means? What do you think each row means? Tell me! (If you're unsure, look at more of the file contents.)**

```
print chipotle.head()
print chipotle.tail()
```

It looks like the file is a collection of Chipotle purchase data. Each column is another relevant piece of data to an order (an ID for the order, a quantity of items, the item's name, a discription of the item if applicable, and the item's price) and each row is a new order. Items with the same order ID appear to be separate items ordered by the same person. 

**2 How many orders do there appear to be?**

```
print chipotle['order_id'].unique().size
```

There appear to be 1834 orders. 

**3 How many lines are in the file?** 

```
print chipotle.count() + 1 #because the indexing is 0 based
```

There are 4623 lines in the file. 4622 values in most columns +1 for the header. 

**4 Which burrito is more popular, steak or chicken?**

```
print chipotle.item_name.value_counts()
```

The chicken burrito is more popular. 

**5 Do chicken burritos more often have black beans or pinto beans?**

```
print chipotle[(chipotle.item_name == 'Chicken Burrito') & (chipotle.choice_description.str.contains('Black Beans'))]
print chipotle[(chipotle.item_name == 'Chicken Burrito') & (chipotle.choice_description.str.contains('Pinto Beans'))]
```
These expressions show us that 282 chicken burritos had black beans and 105 had pinto beans. Black beans happen more often. 

**6 Make a list of all of the CSV or TSV files in the [our class repo] (https://github.com/ga-students/DS-SEA-3). repo (using a single command). You will be working on your local repo on your laptop. Think about how wildcard characters can help you with this task**

**7 Count the approximate number of occurrences of the word "dictionary" (regardless of case) across all files of [our class repo] (https://github.com/ga-students/DS-SEA-3)**


