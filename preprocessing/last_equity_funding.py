import numpy as np
import pandas as pd

def last_equity_funding(df):
    """
    to run before filling empty rounds with zeros
    replace empty 'last_equity_funding_type' by 'series_unknown'
    fill empty 'last_equity_funding_total' by the latest non empty round value
    fill remaining empty 'last_equity_funding_total' with the median of last_equity_funding_type
    drop the remaining line(s) for which we have no amount
    """

    # fill empty 'last_equity_funding_type' with 'series_unknown'
    df['last_equity_funding_type'].fillna("series_unknown",inplace=True)

    # fill empty 'last_equity_funding_total' with the latest non empty round value
    df['last_equity_funding_total'] = np.where(df['last_equity_funding_total'].isnull(), df['Round 5'],df['last_equity_funding_total'])
    df['last_equity_funding_total'] = np.where(df['last_equity_funding_total'].isnull(), df['Round 4'],df['last_equity_funding_total'])
    df['last_equity_funding_total'] = np.where(df['last_equity_funding_total'].isnull(), df['Round 3'],df['last_equity_funding_total'])
    df['last_equity_funding_total'] = np.where(df['last_equity_funding_total'].isnull(), df['Round 2'],df['last_equity_funding_total'])
    df['last_equity_funding_total'] = np.where(df['last_equity_funding_total'].isnull(), df['Round 1'],df['last_equity_funding_total'])

    # compute the median by last_equity_funding_type, merge it to the main dataframe and fill empty 'last_equity_funding_total' with the median
    df_equity_funding_type_median=pd.DataFrame(df[df['last_equity_funding_total'].notnull()].groupby(['last_equity_funding_type']).median()['last_equity_funding_total']).reset_index()
    df_equity_funding_type_median.rename(columns={'last_equity_funding_total':'last_equity_funding_median'},inplace=True)

    df = df.merge(df_equity_funding_type_median, how='left',on='last_equity_funding_type')
    df['last_equity_funding_total'] = np.where(df['last_equity_funding_total'].isnull(), df['last_equity_funding_median'],df['last_equity_funding_total'])
    df.drop('last_equity_funding_median', axis=1,inplace=True)

    # drop the remaining line(s)
    index_to_drop=df[df.last_equity_funding_total.isnull()]['last_equity_funding_total'].index[0]
    df.drop([index_to_drop],inplace=True)

    return df
