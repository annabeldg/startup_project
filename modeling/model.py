import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import cross_validate


def baseline(X, y):
    baseline_model = DummyClassifier(strategy="most_frequent")
    baseline_model.fit(X, y)
    baseline_score=baseline_model.score(X, y)
    return baseline_score

def logistic_regression(X_train, X_test, y_train, y_test):
    model = LogisticRegression(
        C=1.5, class_weight=None, max_iter=1000, random_state=2
        )
    model.fit(X_train, y_train)
    scoring_list=['accuracy', 'recall', 'precision', 'f1']
    cv_results = cross_validate(model, X_test, y_test, cv=5, scoring=scoring_list)
    precision = cv_results['test_precision'].mean()
    return model, precision

def prediction(model, X_new):
    y_pred = model.predict(X_new)

    if y_pred == 0:
        return 'Failure'
    elif y_pred == 1:
        return 'Success'
    else:
        return 'Problem with prediction'
