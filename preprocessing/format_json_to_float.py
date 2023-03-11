import json
import numpy as np

def json_to_float(x):
    '''
    extract the USD amount of json columns
    (last_equity_funding_total and moneyRaised)
    '''
    try:
        return float(json.loads(x)["amountUSD"])
    except:
        return np.nan

    #for column in ['last_equity_funding_total', 'moneyRaised']:
    #    df[column].replace(np.nan,'{"amount": 0, "currency": "USD", "amountUSD": 0}', inplace=True)
    #    df[column].replace('{"value":null,"currency":"USD","value_usd":null}','{"amount": 0, "currency": "USD", "amountUSD": 0}', inplace=True)
    #    df[column] = df[column].map(lambda x: preprocess_moneyRaised(x), na_action='ignore')
