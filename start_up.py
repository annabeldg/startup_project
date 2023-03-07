import os
import pandas as pd

from preprocessing.create_target import create_target
from preprocessing.format_dates_columns import format_dates_columns
from preprocessing.format_last_equity_funding_total_moneyRaised import format_last_equity_funding_total_moneyRaised
from preprocessing.format_object_float_int_columns import format_object_float_int_columns

data_path=os.path.join(os.path.abspath(os.getcwd()),'raw_data')
df=pd.read_csv(os.path.join(data_path,'startups.csv'))
df.drop_duplicates(inplace=True)
df.drop(columns=['website', 'short_description'],inplace = True)

df= format_last_equity_funding_total_moneyRaised(df)
df = format_dates_columns(df)
df = create_target(df)
#df=format_object_float_int_columns(df)

print(df.isnull().sum())
print(df.shape)
