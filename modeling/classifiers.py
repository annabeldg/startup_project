import os
import numpy as np
import pandas as pd

from sklearn.dummy import DummyClassifier

from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# data
data_path=os.path.join(os.path.abspath(os.path.dirname(os.getcwd())),'raw_data')
df=pd.read_csv(os.path.join(data_path,'startups_modified.csv'))

X=df.drop(columns='Target', axis=1)
y=df.Target

X_train, X_test, y_train, y_test = train_test_split(X, y)

baseline_model = DummyClassifier(strategy="most_frequent")
baseline_model.fit(X_train, y_train)
baseline_score=baseline_model.score(X_test, y_test)
print(f'baseline score: {round(baseline_score,2)}')

#model=LogisticRegression(max_iter=1000)
model = KNeighborsClassifier()
#model=RandomForestClassifier()
#model=SVC(kernel='linear', C=10)
#model=SGDClassifier(loss='log_loss')

if type(model).__name__=='RandomForestClassifier':
    grid_dict= {'n_estimators':[10,25,50,100,500,750,1000],'max_depth': [5, 10, 20],'min_samples_split': [2, 5, 10]}
elif type(model).__name__=='LogisticRegression':
    grid_dict= {'penalty':['l2', 'none'],'C':[0.01, 0.1, 0.5, 1, 1.5],'class_weight':['balanced', 'none']}
elif type(model).__name__=='KNeighborsClassifier':
    grid_dict= {'n_neighbors':[1,2,3,4,5]}
elif type(model).__name__=='SVC':
    grid_dict= {'kernel':['linear','poly','rbf','sigmoid'], 'C':[0.01, 0.1, 1],'class_weight':['balanced', 'none']}
elif type(model).__name__=='SGDClassifier':
    grid_dict= {'penalty':['l2', 'l1', 'elasticnet', 'none'],'alpha':[0.01, 0.1,1]}

scoring_list=['accuracy','recall','precision', 'f1']
search = GridSearchCV(model,grid_dict, scoring = scoring_list[2],cv = 5,n_jobs=-1)
search.fit(X_train, y_train)

print(f'best estimator: {search.best_estimator_}')
print(f'best score: {round(search.best_score_,2)}')

model=search.best_estimator_

y_true = y_test
y_pred = model.predict(X_test)

print('Accuracy =', round(accuracy_score(y_true, y_pred), 2)) # Accuracy
print('Precision =', round(precision_score(y_true, y_pred), 2)) # Precision
print('Recall =', round(recall_score(y_true, y_pred), 2)) # Recall
print('F1 score =', round(f1_score(y_true, y_pred), 2)) # F1 score
