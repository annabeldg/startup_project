
import pandas as pd

def format_dates(df, column_list):
    '''
    format selected columns to date
    '''

    df[column_list] = df[column_list].apply(pd.to_datetime)

    return df
