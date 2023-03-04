
def format_object_float_int_columns(df):
    '''
    format object, float and int columns
    remove website and short_description columns
    '''

    column_types=['object', 'int64', 'float64']

    for column_type in column_types:

        columns_to_fill= df.select_dtypes(include=column_type).columns.to_list()

        for column_to_fill in columns_to_fill:

            if df[column_to_fill].isnull().sum()!=0:

                if column_type=='object':

                    df[column_to_fill].fillna("none",inplace=True)

                else:

                    if column_to_fill !='time_to_success':

                        df[column_to_fill].fillna(0,inplace=True)

    df.drop(columns=['website', 'short_description'],inplace = True)

    return df
