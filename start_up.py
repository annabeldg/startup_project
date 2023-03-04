import os
import pandas as pd
import numpy as np

from preprocessing.format_dates import format_dates
from preprocessing.create_target import create_target

data_path=os.path.join(os.path.abspath(os.getcwd()),'raw_data')
df=pd.read_csv(os.path.join(data_path,'data_startup_final.csv'))
df.drop_duplicates(inplace=True)

date_columns=['founded_on', 'went_public_on', 'exited_on','last_funding_at','announcedOn']

df = format_dates(df, date_columns)
df = create_target(df)
