import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

to_scale = ['num_funding_rounds', 'last_equity_funding_total', 'employeeCount',
            'Round 1', 'Round 2', 'Round 3', 'Round 4', 'Round 5',
            'days_between_dates']

minmax = ['Round 1', 'Round 2', 'Round 3', 'Round 4', 'Round 5']

def scale_standard(df):
    '''
    Standard-scale the following features:
    ['num_funding_rounds',
     'last_equity_funding_total',
     'employeeCount',
     'days_between_dates']
    '''

    standard = ['num_funding_rounds',
                'last_equity_funding_total',
                'employeeCount',
                'days_between_dates']

    scaler = StandardScaler()

    scaler.fit(df[standard])

    df[standard] = scaler.transform(df[standard])


def scale_minmax(df):
    '''
    Minmax-scale the following features:
    ['Round 1', 'Round 2', 'Round 3', 'Round 4', 'Round 5']
    '''

    minmax = ['Round 1', 'Round 2', 'Round 3', 'Round 4', 'Round 5']

    scaler = MinMaxScaler()

    scaler.fit(df[minmax])

    df[minmax] = scaler.transform(df[minmax])
