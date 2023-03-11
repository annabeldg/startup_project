# change 'founded_on' and last 'last_funding_at' to a date

import pandas as pd
import datetime as dt

def calculate_days_between_dates(df):

    # to datetime
    for column in ['last_funding_at', 'founded_on']:
        df[column] = pd.to_datetime(df[column])

    # calculate the difference between last_funding_at and founded_on in days
    df["days_between_dates"] = (df["last_funding_at"] - df["founded_on"]).dt.days

    # drop the original founded_on and last_funding_at columns
    df = df.drop(["founded_on", "last_funding_at"], axis=1)

    # return the updated dataframe
    return df
