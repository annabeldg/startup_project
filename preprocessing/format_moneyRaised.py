import json
import numpy as np

def format_moneyRaised(df):
    '''
    extract the USD amount of column moneyRaised, convert to float and store it to column 'moneyRaised_USD'
    '''

    def preprocess_moneyRaised(x):
        return float(json.loads(x)["amountUSD"])/100

    df['moneyRaised'].replace(np.nan,'{"amount": 0, "currency": "USD", "amountUSD": 0}', inplace=True)
    df['moneyRaised_USD'] = df['moneyRaised'].apply(lambda x: preprocess_moneyRaised(x))
    df.drop(columns='moneyRaised',inplace = True)

    return df
