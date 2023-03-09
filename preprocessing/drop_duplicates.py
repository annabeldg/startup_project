import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Do not forget to df.drop_duplicates the original raw dataset :)

def industry_encoding(data):
    '''
    Returns all one-hot-encoded columns of industry_name feature as a df.

    The structure is the following:
    df.columns = ['id', 'industry_1', 'industry_2', ..., 'industry_n']
    '''
    # Drop duplicates after restricting df to industry_name
    data_ind = data[['id', 'industry_name']].drop_duplicates()

    # One hot encode all possible industries
    encoder = OneHotEncoder(sparse=False)
    data_ind[encoder.get_feature_names_out()] = encoder.fit_transform(data_ind[['industry_name']])

    # Rename one hot encoded columns in a more desirable way
    for column in data_ind.columns[2:]:
        data_ind.rename(columns={column: column[14:]}, inplace=True)

    # Group by id to get one column for each company and keep max value of
    # one hot encoded features to have all possible industries = 1 on one line
    data_ind = data_ind.groupby('id').max()

    # Reset_index and drop useless features
    data_ind.reset_index(inplace=True)
    data_ind.drop(columns=['nan', 'industry_name'], inplace=True)

    return data_ind


def technology_encoding(data):
    '''
    Returns all one-hot-encoded columns of technology_name feature as a df.

    The structure is the following:
    df.columns = ['id', 'technology_1', 'technology_2', ..., 'technology_n']
    '''
    # Drop duplicates after restricting df to technology_name
    data_tec = data[['id', 'technology_name']].drop_duplicates()

    # One hot encode all possible technologies
    encoder = OneHotEncoder(sparse=False)
    data_tec[encoder.get_feature_names_out()] = encoder.fit_transform(data_tec[['technology_name']])

    # Rename one hot encoded columns in a more desirable way
    for column in data_tec.columns[2:]:
        data_tec.rename(columns={column: column[16:]}, inplace=True)

    # Group by id to get one column for each company and keep max value of
    # one hot encoded features to have all possible technologies = 1 on one line
    data_tec = data_tec.groupby('id').max()

    # Reset_index and drop useless features
    data_tec.reset_index(inplace=True)
    data_tec.drop(columns=['nan', 'technology_name'], inplace=True)

    return data_tec


def funding_encoding(data):
    '''
    Returns funding round amounts in a chronological order. Funding rounds for
    a particular company are expanded on multiple columns, max 5. For example,
    if Apple has raised 200 is round 1, 1000 in round 2, and 3000 in round 3:

                Round 1     Round 2     Round 3     Round 4     Round 5
    Apple       200         1000        3000        NaN         NaN
    '''

    # Restrict and drop duplicates
    data_fun = data[['id', 'announcedOn', 'moneyRaised']].drop_duplicates()

    # Convert announcedOn to datetime and sort companies by date
    data_fun['announcedOn'] = pd.to_datetime(data_fun['announcedOn'])
    data_fun.sort_values(by=['id', 'announcedOn'], inplace=True)

    # Use Baptiste's function to transform money raised from json --> int
    # format_last_equity_funding_total_moneyRaised(data_fun)

    ## SET THE FOLLOWING BEFORE MY PART
    #def preprocess_moneyRaised(x):
    #    return float(json.loads(x)["amountUSD"])

    #data_fun['moneyRaised'] = data_fun['moneyRaised'].map(lambda x: preprocess_moneyRaised(x), na_action='ignore')

    # Convert money raised to real value (before, forgot the two decimals)
    data_fun['moneyRaised'] = data_fun['moneyRaised']/100

    # Drop columns we don't need anymore and rows that raised 0 USD
    data_fun.drop(columns=['announcedOn'], inplace=True)
    data_fun = data_fun[data_fun['moneyRaised'] != 0]
    data_fun = data_fun[data_fun['moneyRaised'].isnull() == False]

    # Add the occurence number of a company id
    data_fun['index'] = data_fun.groupby('id').cumcount() + 1

    # Pivot the data to create the desired output
    output = data_fun.pivot(index='id', columns='index', values='moneyRaised')

    # Rename the columns to match the desired output and reset index
    output.columns = [str(i) for i in output.columns]
    data_fun = output
    data_fun.reset_index(inplace=True)

    # Restrict to maximum 5 funding rounds
    data_fun = data_fun.iloc[:, 0:6]

    # Rename funding round number columns in a more desirable way
    for i in range(1, 6):
        data_fun.rename(columns={str(i): f'Round {str(i)}'}, inplace=True)

    return data_fun


def merged_all(main_df, industry_df, technology_df, funding_df):
    '''
    Merge one hot encoded industries, one hot encoded technologies, and funding
    rounds to the main dataframe.
    '''

    # Drop columns that multiply duplicates then drop duplicates
    data_merged = main_df.drop(columns=['industry_name',
                                        'technology_name',
                                        'announcedOn',
                                        'moneyRaised'])
    data_merged = data_merged.drop_duplicates().reset_index(drop=True)

    # Merge industry dataframe
    data_merged_ind = data_merged.merge(industry_df, on='id', how='left')
    #print(data_merged_ind.shape)

    # Merge technology dataframe
    data_merged_tec = data_merged_ind.merge(technology_df, on='id', how='left')
    #print(data_merged_tec.shape)

    # Merge funding round dataframe
    data_merged_all = data_merged_tec.merge(funding_df, on='id', how='left')
    #print(data_merged_all.shape)

    return data_merged_all
