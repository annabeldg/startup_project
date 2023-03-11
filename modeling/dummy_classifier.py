from sklearn.dummy import DummyClassifier

import os
import numpy as np
import pandas as pd


from create_X_y import create_X_y
from train_test_split import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from sklearn.model_selection import cross_validate, train_test_split, learning_curve, GridSearchCV

import warnings
warnings.filterwarnings("ignore")

# data - to remove
data_path=os.path.join(os.path.abspath(os.path.dirname(os.getcwd())),'raw_data')

df=pd.read_csv(os.path.join(data_path,'startups_modified.csv'))
df=df[df.select_dtypes(include=['int64', 'float64']).columns.to_list()]
df.fillna(0, inplace =True)

X, y = create_X_y(df)

#scaling-to remove
scaler=StandardScaler()
columns_to_scale=['num_funding_rounds', 'last_equity_funding_total', 'employeeCount','Round 1','Round 2', 'Round 3', 'Round 4', 'Round 5']
X[columns_to_scale]=scaler.fit_transform(X[columns_to_scale])

X_train, X_test, y_train, y_test = train_test_split(X, y)

baseline_model = DummyClassifier(strategy="most_frequent") # Baseline
baseline_model.fit(X_train, y_train) # Calculate value for stratgy
baseline_score=baseline_model.score(X_test, y_test)

print(baseline_score)
