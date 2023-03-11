def create_X_y(df):

    X=df.drop(columns='Target', axis=1)
    y=df.Target

    return X, y
