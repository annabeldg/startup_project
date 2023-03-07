import os
import pandas as pd

from preprocessing.create_target import create_target
from preprocessing.format_dates_columns import format_dates_columns
from preprocessing.format_last_equity_funding_total_moneyRaised import format_last_equity_funding_total_moneyRaised
from preprocessing.format_object_float_int_columns import format_object_float_int_columns

from preprocessing.drop_duplicates import industry_encoding, technology_encoding, funding_encoding, merged_all

# Read our main database, the startups.csv
data_path = os.path.join(os.path.abspath(os.getcwd()),'raw_data')
df = pd.read_csv(os.path.join(data_path,'startups.csv'))
print('Dataset successfully read!')

## DROP PROPER DUPLICATES ##

df.drop_duplicates(inplace=True)

## STARTING PREPROCESSING TASKS ##

# Convert last_equity_funding_total and moneyRaised columns from json to float
df = format_last_equity_funding_total_moneyRaised(df)

# Format dates columns to datetime
df = format_dates_columns(df) #missing values in columns: went_public_on, exited_on, announcedOn

## ENCODING ##

# Encode industry, technology, and funding_rounds columns as a separate dataframe
data_ind = industry_encoding(df)
data_tec = technology_encoding(df)
data_fun = funding_encoding(df)

# Merge all in the main df
data_encoded = merged_all(df, data_ind, data_tec, data_fun)


# Encode the target variable
data_encoded = create_target(data_encoded) #missing values in columns: time_to_success

# Encode last_equity_funding_type!!
print(data_encoded.shape)

data_encoded.to_csv(os.path.join(data_path, 'startups_modified.csv'), index=False)
