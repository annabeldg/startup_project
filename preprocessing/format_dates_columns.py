import datetime
import pandas as pd

def format_dates_columns(df):
    '''
    format date columns to date
    '''

    date_columns=['founded_on', 'went_public_on', 'exited_on','last_funding_at','announcedOn']
    df[date_columns] = df[date_columns].apply(pd.to_datetime)

    #for date_column in date_columns:
        #if df[date_column].isnull().sum()!=0:
            #df[date_column].fillna(datetime.datetime.min,inplace=True)

    return df
