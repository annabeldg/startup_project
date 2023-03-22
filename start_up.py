import os
import pandas as pd
import numpy as np
import pickle
import shap

from preprocessing.create_target import create_target
from preprocessing.format_json_to_float import json_to_float
from preprocessing.encode import replace_rare_values_with_others, one_hot_encode_region, drop_columns
from preprocessing.encode import one_hot_encode_last_equity_funding_type
from preprocessing.engineer import calculate_days_between_dates
from preprocessing.missing_data import miss_total, miss_hq, miss_employee, miss_round1, miss_round2345
from preprocessing.outliers import outlier_rounds, outlier_total
from preprocessing.scaling import scale_standard, scale_minmax
from preprocessing.drop_duplicates import industry_encoding, technology_encoding, funding_encoding, merged_all
from preprocessing.smote import smote_resample
from preprocessing.remove_post_ipo_equity import remove_post_ipo_equity

from sklearn.model_selection import train_test_split
from modeling.model import baseline, logistic_regression, prediction

from useful.variables import regions

# Read our main database, the startups.csv
data_path = os.path.join(os.path.abspath(os.getcwd()),'raw_data')
df = pd.read_csv(os.path.join(data_path,'startups.csv'))
print('Dataset successfully read!')

## 0. DROP LINES WHERE last_equity_funding_type']!='post_ipo_equity' ##
#print(df.shape)
#df=remove_post_ipo_equity(df)
#print(df.shape)

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

print('Remove duplicates: Success')

## 3. ENCODING & FEATURE ENGINEERING THE REST ##

# Drop useless columns
data_nodup.drop(columns=['id', 'name', 'website', 'short_description', 'ipo_status', 'headquartersRegion'],
                inplace=True)

# Extract float from json in last_equity_funding_total
data_nodup['last_equity_funding_total'] = data_nodup['last_equity_funding_total'].map(
    lambda x: json_to_float(x), na_action='ignore'
    )
data_nodup['last_equity_funding_total'] = data_nodup['last_equity_funding_total']/100

# Divide countries by region and one hot encode them
#data_nodup = replace_rare_values_with_others(data_nodup, 'headquartersCountry')
data_nodup['headquartersCountry'] = data_nodup['headquartersCountry'].map(lambda x: regions[x], na_action='ignore')
data_nodup.rename(columns={'headquartersCountry': 'region'}, inplace=True)
ohe_regions = one_hot_encode_region(data_nodup, 'region')
ohe_regions.drop(columns=[np.nan], inplace=True)
data_nodup = data_nodup.join(ohe_regions)

# One hot encode last_equity_funding_type
left = one_hot_encode_last_equity_funding_type(data_nodup, 'last_equity_funding_type')
left = drop_columns(left)
data_nodup = data_nodup.join(left)

# Engineer the number of days between last_funding_at and founded_on
data_nodup = calculate_days_between_dates(data_nodup)

# Encode the target variable
data_encoded = create_target(data_nodup)

print('Features encoded: Success')


## 4. MISSING DATA ##

# Fill missing values for last_equity_funding_total
data_encoded = miss_total(data_encoded)
data_encoded.drop(columns='last_equity_funding_type', inplace=True)

# Remove rows where region in NaN
data_encoded = miss_hq(data_encoded)
data_encoded.drop(columns='region', inplace=True)

# Replace missing values of employeeCount by the median
miss_employee(data_encoded)

# Replace missing values of Round 1 with last_equity_funding_total
data_encoded = miss_round1(data_encoded)

# Replace missing values of Round 2 -> 5 by 0
data_filled = miss_round2345(data_encoded)

print('Handle missing values: Success')


## 5. OUTLIERS ##

# Keep rows where $50,000 < last_equity_funding_total < $200,000,000
data_filled = outlier_total(data_filled)

# Keep rows where $50,000 < Round 1->5
data_noout = outlier_rounds(data_filled)

print('Remove outliers: Success')

## 6. SCALING ##

# Standard-scale employees, funding total, number of rounds, and days
scale_standard(data_noout)

# Minmax-scale Round 1 to 5
scale_minmax(data_noout)
data_scaled = data_noout

print('Feature scaling: Success')
print(data_scaled.shape)

## 8. MODELLING ##

# Divide features and targets
X = data_scaled.drop(columns='Target')
y = data_scaled['Target']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)

# Perform a smote on train set
X_train, y_train = smote_resample(X_train, y_train, ratio=0.3)
print('SMOTE balancing: Success')

# FOR VIZ PURPOSES: reconcatenate
data_balanced = X_train.join(y_train)
data_balanced.to_csv(os.path.join(data_path, 'startups_modified.csv'), index=False)

# Compute baseline score
baseline_score = baseline(X_train, y_train)
print(f'Baseline score: {round(baseline_score,2)}')

# Logistic regression
model, precision = logistic_regression(X_train, X_test, y_train, y_test)
print(f'Model precision: {str(precision)}')

# Save model
pickle.dump(model, open('modeling/startup_model.pkl', 'wb'))

#Shap
explainer = shap.LinearExplainer(model, X_train)
pickle.dump(explainer, open('modeling/shap_explainer.pkl', 'wb'))

# Prediction
# y_pred = prediction(model, X_new)


# TEMPORARY: reconcatenate
# data_balanced = X.join(y)

#print(data_balanced.shape)

#data_balanced.to_csv(os.path.join(data_path, 'startups_modified.csv'), index=False)

## IF WE HAVE SOME TIME ##

# 1. Keep announcedOn of the first round
# 2. NLP on short_description
# 3.
