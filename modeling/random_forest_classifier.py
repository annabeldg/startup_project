from sklearn.ensemble import RandomForestClassifier

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

data_path=os.path.join(os.path.abspath(os.path.dirname(os.getcwd())),'raw_data')

df=pd.read_csv(os.path.join(data_path,'startups_modified.csv'))
df=df[df.select_dtypes(include=['int64', 'float64']).columns.to_list()]
df.fillna(0, inplace =True)

X, y = create_X_y(df)

#scaling-to remove
scaler=StandardScaler()
columns_to_scale=['num_funding_rounds', 'last_equity_funding_total', 'employeeCount','Round 1','Round 2', 'Round 3', 'Round 4', 'Round 5','days_between_dates']
X[columns_to_scale]=scaler.fit_transform(X[columns_to_scale])

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = RandomForestClassifier()
grid_dict= {'n_estimators':[10,25,50,100,500,750, 1000]}
scoring_list=['accuracy','recall','precision', 'f1']
search = GridSearchCV(model,grid_dict, scoring = scoring_list[2],cv = 5,n_jobs=-1)
search.fit(X_train, y_train)

print(f'best score: {search.best_score_}')
print(f'best params: {search.best_params_}')
print(f'best estimator: {search.best_estimator_}')

model=search.best_estimator_

y_true = y_test
y_pred = model.predict(X_test)

print('Accuracy =', round(accuracy_score(y_true, y_pred), 3)) # Accuracy
print('Precision =', round(precision_score(y_true, y_pred), 3)) # Precision
print('Recall =', round(recall_score(y_true, y_pred), 3)) # Recall
print('F1 score =', round(f1_score(y_true, y_pred), 3)) # F1 score
