from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import roc_auc_score
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, max_error
import math
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

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

# let's select whcih model is best fitted WITHOUT multicolinearity checks

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


# let's check for mulicolineraity --> Error message if there is some, otherwise fit the model

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from statsmodels.stats.outliers_influence import variance_inflation_factor

def train_model_without_colinearity(data):
    
    y = data["target"]
    X = data.drop("target", axis=1)
    
    # Check for multicollinearity
    vif = pd.DataFrame()
    vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    vif["features"] = X.columns
    high_vif = vif[vif['VIF Factor'] > 10]
    
    # If there is a high VIF value, output an error message and return
    if len(high_vif) > 0:
        print("There is a multicollinearity issue with the data. High VIF detected for the following features:")
        print(high_vif)
        return None
    
    # If there are no high VIF values, proceed with scaling and training the model
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    pca = PCA(n_components=0.95)
    X_pca = pca.fit_transform(X_scaled)
    
    if X_pca.shape[1] > 10:
        model = RandomForestClassifier()
    else:
        model = LogisticRegression()
        
    model.fit(X_pca, y)
    
    y_pred = model.predict_proba(X_pca)[:, 1]
    print("AUC-ROC score: {:.4f}".format(roc_auc_score(y, y_pred)))
    
    return model

# makes predictions on the test data, and evaluates the model using mean squared error (MSE), root mean squared error (RMSE), mean absolute error (MAE), R-squared, and maximum error.
# uses Lasso to feature selection 

def regression_pipeline(data, alpha=1.0):
    # Step 1: Splitting data and building a baseline model
    y = data["target"]
    X = data.drop("target", axis=1)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=6)

    baseline_model = DummyRegressor(strategy="mean")
    baseline_model.fit(X_train, y_train)
    baseline_score = baseline_model.score(X_test, y_test)
    
    # Step 2: Feature selection using Lasso
    model = Lasso(alpha=alpha)
    model.fit(X_train, y_train)
    
    selected_features = X.columns[model.coef_ != 0]
    X_train = X_train[selected_features]
    X_test = X_test[selected_features]
    
    # Step 3: Fit and evaluate the regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    rmse = math.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    rsquared = r2_score(y_test, y_pred)
    max_error = max_error(y_test, y_pred)

    print('Baseline score =', round(baseline_score, 2))
    print('Selected features:', list(selected_features))
    print('MSE =', round(mse, 2))
    print('RMSE =', round(rmse, 2))
    print('MAE =', round(mae, 2))
    print('R2 =', round(rsquared, 2))
    print('Max Error =', round(max_error, 2))
    
    return model

# Create NLP to add the model an analyis of the keywords most used in the company description

def nlp_feature(data):
    
    # Remove punctuation
    data["Short description"] = data["Short description"].apply(lambda text: text.translate(str.maketrans('', '', string.punctuation)))
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    data["Short description"] = data["Short description"].apply(lambda text: ' '.join([word for word in text.split() if word.lower() not in stop_words]))
    
    # Create the bag of words
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data["Short description"])
    
    # Split the data
    y = data["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train the model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Print the accuracy score
    print("Accuracy: {:.2f}%".format(model.score(X_test, y_test) * 100))
    
    # Return the trained model
    return model

