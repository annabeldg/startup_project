import numpy as np
import pandas as pd


def outlier_total(df):
    '''
    Keep values of last_equity_funding_total that are $50,000 < $x < $200,000,000
    '''

    df = df[(df["last_equity_funding_total"] >= 50000) & (df["last_equity_funding_total"] <= 200000000)]

    return df

def outlier_rounds(df):
    '''
    Keep values of Rounds that are $50,000 < $x
    '''
    df = df[df['Round 1'] != 0]

    for i in range(2, 6):
        df = df[(df[f'Round {i}'] >= 50000) | (df[f'Round {i}'] == 0)]

    return df
