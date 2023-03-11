from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score

def tune_hyperparameters(data):
    
    y = data["target"]
    X = data.drop("target", axis=1)
    
    # Define the model
    model = RandomForestRegressor()

    # Define the grid of hyperparameters to search over
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [5, 10, 20],
        'min_samples_split': [2, 5, 10]
    }

    # Define the search strategy
    search = GridSearchCV(model, param_grid, scoring='neg_mean_squared_error', cv=5)

    # Perform the search
    search.fit(X, y)

    # Print the best hyperparameters and score
    print("Best hyperparameters: ", search.best_params_)
    print("Best score: ", -search.best_score_)
    
    # Return the best model
    best_model = search.best_estimator_
    return best_model

# let's select whcih model is best fitted

def train_model(data):
    
    y = data["target"]
    X = data.drop("target", axis=1)
    
    # Determine which model to use
    if X.shape[1] > 10:
        # Use a decision tree-based model for large datasets
        model = RandomForestClassifier()
    else:
        # Use a logistic regression model for small datasets
        model = LogisticRegression()
        
    # Train the model
    model.fit(X, y)
    
    # Print the AUC-ROC score
    y_pred = model.predict_proba(X)[:, 1]
    print("AUC-ROC score: {:.4f}".format(roc_auc_score(y, y_pred)))
    
    # Return the trained model
    return model


