import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unique_values = data['whoAmI'].unique()

one_hot_encoded = pd.DataFrame()

for value in unique_values:
    one_hot_encoded[value] = (data['whoAmI'] == value).astype(int)

print(one_hot_encoded.head())
