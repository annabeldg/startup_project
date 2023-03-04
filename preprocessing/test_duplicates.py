import pandas as pd

from preprocessing.drop_duplicates import industry_encoding, technology_encoding, funding_encoding, merged_all

data = pd.read_csv('/Users/danyhersco/startups.csv')
data = data.drop_duplicates()

data_ind = industry_encoding(data)
data_tec = technology_encoding(data)
data_fun = funding_encoding(data)
data_merged = merged_all(data, data_ind, data_tec, data_fun)

print(data_merged)
