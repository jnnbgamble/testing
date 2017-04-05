#import requests as r
import pandas as pd
path = 'data/chipotle.tsv'

chipotle = pd.DataFrame.from_csv(path, sep='\t')

print chipotle.tail()