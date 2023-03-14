import pandas as pd
from imblearn.over_sampling import SMOTE

def smote_resample(X, y, ratio=0.3):
    '''
    Perform a SMOTE on the dataset. Ratio is the percentage occurence of
    startup success among all startups, which by default is 30%.
    '''

    over = SMOTE(sampling_strategy=ratio, random_state=1)
    X, y = over.fit_resample(X, y)

    return X, y
