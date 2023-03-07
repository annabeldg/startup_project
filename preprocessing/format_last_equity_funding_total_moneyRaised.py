import json
import numpy as np

def format_last_equity_funding_total_moneyRaised(df):
    '''
    extract the USD amount of columns last_equity_funding_total and moneyRaised, convert to float and store it in the original columns
    '''

    def preprocess_moneyRaised(x):
        try:
            return float(json.loads(x)["amountUSD"])
        except:
            pass

    for column in ['last_equity_funding_total', 'moneyRaised']:
        #df[column].replace(np.nan,'{"amount": 0, "currency": "USD", "amountUSD": 0}', inplace=True)
        #df[column].replace('{"value":null,"currency":"USD","value_usd":null}','{"amount": 0, "currency": "USD", "amountUSD": 0}', inplace=True)
        df[column] = df[column].apply(lambda x: preprocess_moneyRaised(x))

    return df
