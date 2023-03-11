## STRATEGY ##

# last_equity_funding_total:
# Remove < 20,000
# Remove > 1,000,000,000

# Finally don't touch Round 1 -> 5


prone_to_outliers = ['last_equity_funding_total', 'Round 1 --> 5']

import numpy as np
import pandas as pd

def clean_database(db):
    # Replace NaN values in Round 1 with the mean of Round 1
    round_1_mean = db["Round 1"].mean(skipna=True)
    db["Round 1"] = db["Round 1"].fillna(round_1_mean)
    
    # Replace NaN values in Round 2, Round 3, Round 4, and Round 5 with 0
    db[["Round 2", "Round 3", "Round 4", "Round 5"]] = db[["Round 2", "Round 3", "Round 4", "Round 5"]].fillna(0)
    
    # Replace NaN values in last_equity_funding_total with the maximum value between Round 1-5
    db["last_equity_funding_total"] = db[["Round 1", "Round 2", "Round 3", "Round 4", "Round 5"]].max(axis=1)
    db["last_equity_funding_total"] = db["last_equity_funding_total"].fillna(0)
    
    # Remove outliers in last_equity_funding_total
    db = db[(db["last_equity_funding_total"] >= 20000) & (db["last_equity_funding_total"] <= 1000000000)]
    
    return db
