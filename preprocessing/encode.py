import pandas as pd
import numpy as np
from useful.variables import regions

def one_hot_encode_last_equity_funding_type(data, column):

    # Get unique values
    unique_values = data[column].unique()

    # Create a dictionary to map each unique value to a binary feature
    feature_dict = {value: [1 if value == val else 0 for val in unique_values] for value in unique_values}

    # Convert data to binary features using one-hot encoding
    binary_data = []
    for value in data[column]:
        binary_data.append(feature_dict.get(value, [0]*len(unique_values)))

    # Convert binary data to a pandas DataFrame
    binary_df = pd.DataFrame(binary_data, columns=unique_values)

    return binary_df

def continuous_encode(data, column):

    # Group the data by the values in the specified column and count the number of occurrences of each value
    counts = data.groupby(column).size()

    # Sort the counts in descending order and convert them to a dictionary
    count_dict = counts.sort_values(ascending=False).to_dict()

    # Create a new DataFrame with the continuous encoding
    encoding = pd.DataFrame(data[column].map(count_dict))

    return encoding


# STEP 1 --> Get ride of some columns --> Concatenate them in others

import pandas as pd

def replace_rare_values_with_others(data, column):
    # Count the number of occurrences of each value
    value_counts = data[column].value_counts()

    # Get values that appear fewer than 2 times
    rare_values = value_counts[value_counts < 50].index.tolist()

    # Replace rare values with "OTHERS"
    data[column] = data[column].apply(lambda x: "OTHERS" if x in rare_values else x)

    return data

# STEP 2 --> Encode

def one_hot_encode_region(data, column):

    # Get unique values
    unique_values = data[column].unique()

    # Create a dictionary to map each unique value to a binary feature
    feature_dict = {value: [1 if value == val else 0 for val in unique_values] for value in unique_values}

    # Convert data to binary features using one-hot encoding
    binary_data = []
    for value in data[column]:
        binary_data.append(feature_dict.get(value, [0]*len(unique_values)))

    # Convert binary data to a pandas DataFrame
    binary_df = pd.DataFrame(binary_data, columns=unique_values)

    return binary_df

# Clean last equity funding

def drop_columns(data):

    # Change according to threshold but here are all of them

    columns_to_drop = [np.nan, "series_unknown", "undisclosed","corporate_round", "initial_coin_offering"]

    #columns_to_drop = [np.nan, "series_unknown", "undisclosed","corporate_round", "initial_coin_offering", "post_ipo_equity"]

    data.drop(columns=columns_to_drop, inplace=True)

    return data
