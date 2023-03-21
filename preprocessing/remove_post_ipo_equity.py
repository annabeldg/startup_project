def remove_post_ipo_equity(df):

    df=df[df['last_equity_funding_type']!='post_ipo_equity']
    return df
