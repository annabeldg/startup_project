import os
import pandas as pd

from preprocessing.create_target import create_target
from preprocessing.format_dates_columns import format_dates_columns
from preprocessing.format_last_equity_funding_total_moneyRaised import format_last_equity_funding_total_moneyRaised
from preprocessing.format_object_float_int_columns import format_object_float_int_columns

data_path=os.path.join(os.path.abspath(os.getcwd()),'raw_data')
df=pd.read_csv(os.path.join(data_path,'data_startup_final.csv'))
df.drop_duplicates(inplace=True)

df= format_last_equity_funding_total_moneyRaised(df)
df = format_dates_columns(df) #missing values in columns: went_public_on, exited_on, announcedOn
df = create_target(df) #missing values in columns: time_to_success
df=format_object_float_int_columns(df) #to check, notably last_equity_funding_type and stage

print(df.shape)
