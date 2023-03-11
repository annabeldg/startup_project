import os
import pandas as pd

from preprocessing.create_target import create_target
from preprocessing.format_json_to_float import json_to_float
from preprocessing.format_object_float_int_columns import format_object_float_int_columns

from preprocessing.drop_duplicates import industry_encoding, technology_encoding, funding_encoding, merged_all

# Read our main database, the startups.csv
data_path = os.path.join(os.path.abspath(os.getcwd()),'raw_data')
df = pd.read_csv(os.path.join(data_path,'startups.csv'))
print('Dataset successfully read!')

## 1. DROP PROPER DUPLICATES ##

df.drop_duplicates(inplace=True)

## 2. DROP LEFT-JOINED DUPLICATES (+ ENCODING OF INDUSTRY, TECHNOLOGY, ROUNDS) ##

# Convert moneyRaised columns from json to float
df['moneyRaised'] = df['moneyRaised'].map(lambda x: json_to_float(x), na_action='ignore')

# Encode industry, technology, and funding_rounds columns as a separate dataframe
data_ind = industry_encoding(df)
data_tec = technology_encoding(df)
data_fun = funding_encoding(df)

# Merge all in the main df
data_nodup = merged_all(df, data_ind, data_tec, data_fun)

## 3. ENCODING & FEATURE ENGINEERING THE REST ##

# Drop useless columns
data_nodup.drop(columns=['id', 'name', 'website', 'short_description', 'ipo_status', 'headquartersRegion'],
                inplace=True)

to_encode = ['last_equity_funding_type', 'last_equity_funding_total', 'headquartersCountry']
to_engineer = ['founded_on', 'last_funding_at']

# Encode the target variable
data_encoded = create_target(data_nodup) #missing values in columns: time_to_success

## 4. OUTLIERS ##

prone_to_outliers = ['last_equity_funding_total', 'Round 1 --> 5']
# Do not forget to /100 last_equity_funding_total

## 5. MISSING DATA ##

columns_where_misses = ['last_equity_funding_type', 'last_equity_funding_total'
                        'headquartersCountry', 'employeeCount', 'Round 1-->5']

## 6. SCALING ##


print(data_encoded.shape)



data_encoded.to_csv(os.path.join(data_path, 'startups_modified.csv'), index=False)

## IF WE HAVE SOME TIME ##

# 1. Keep announcedOn of the first round
# 2. NLP on short_description
# 3.
