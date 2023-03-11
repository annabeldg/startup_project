import pandas as pd
import numpy as np

## STRATEGY ##

# 'last_equity_funding_type':
# if there is total, replace by the type in which the total is in its range, else remove

# 'last_equity_funding_type':
# if there is type, replace by the median of its range, else remove

# 'hq': if not here remove

# 'employeeCount':
# Replace by the median

# Round 1:
# NaN to be filled by last_equity_funding_type
# Round 2 --> 5:
# NaN to be replaced by 0

def miss_hq(df):
    '''
    Startegy: remove rows where headquartersCountry is NaN
    '''

    df['headquartersCountry']
