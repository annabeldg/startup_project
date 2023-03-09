import pandas as pd

def one_hot_encode(data, column):
   
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