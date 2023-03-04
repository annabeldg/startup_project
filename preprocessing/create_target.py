def create_target(df):
    '''
    create target:
    - target = 1 if went_public_on or exited_on columns are not empty
    - target = 0 otherwise

    create time to success column in days

    we can see that:
    - if went_public_on is not null then exited_on is not null and exited_on = went_public_on except for a few cases
    - went_public_on can be null when exited_on is not
    '''

    df.loc[(df.went_public_on.notnull()) | (df.exited_on.notnull()), 'Target'] = 1
    df.loc[(df.went_public_on.isnull()) & (df.exited_on.isnull()), 'Target'] = 0

    df.loc[(df.Target==1) & (df.exited_on.notnull()), 'time_to_success'] = df['exited_on']-df['founded_on']
    df.loc[(df.Target==1) & (df.went_public_on.notnull()), 'time_to_success'] = df['went_public_on']-df['founded_on']

    return df
