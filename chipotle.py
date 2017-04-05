#import requests as r
import pandas as pd
path = 'data/chipotle.tsv'
#headings = ['order_id', 'quantity', 'item_name', 'choice_description', 'item_price']

#chipotle = pd.DataFrame.from_csv(path, sep='\t')
chipotle = pd.read_csv(path, sep='\t')

#print chipotle.tail(3)

print chipotle['order_id'].unique().size
#print chipotle.count()

#print chipotle['item_name']

#print chipotle.item_name.value_counts() Prints 

print type(chipotle.choice_description)
                                      
print chipotle[chipotle.item_name == 'Chicken Burrito' & chipotle.choice_description.str.contains('Black Beans')]
