import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()


heads = data['whoAmI'].unique()
one_hot_view = pd.DataFrame()
for el in heads:
    one_hot_view[el] = (data['whoAmI'] == el).astype(int)
print(one_hot_view)
