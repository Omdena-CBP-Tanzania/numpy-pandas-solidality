import numpy as np
import pandas as pd

def create_1d_array():
    arr=np.array([1,2,3,4,5])
    return create_1d_array
    """
    Create a 1D NumPy array with values [1, 2, 3, 4, 5]
    Returns:
        numpy.ndarray: 1D array
    """
    pass

def create_2d_array():
    arr=np.array([1,2,3],[5,6,7])
    return(create_2d_array)
    """
    Create a 2D NumPy array with shape (3,3) of consecutive integers
    Returns:
        numpy.ndarray: 2D array
    """
    pass

def array_operations(arr):
    arr.mean()
    arr.std()
    arr.max()
    return(array_operations)
    """
    Perform basic array operations:
    1. Calculate mean
    2. Calculate standard deviation
    3. Find max value
    Returns:
        tuple: (mean, std_dev, max_value)
    """
    pass

def read_csv_file(filepath):
    sample_dt = {
        'Name': ['Zuberi', 'John', 'Monica', 'Ammy'],
        'Age': [25, np.nan, 30, 35],
        'Salary': [500, 600, np.nan, 750]
    }
    df = pd.DataFrame(sample_dt)
    df.to_csv('sample_dt.csv', index=False)
    return(read_csv_file)
    """
    Read a CSV file using Pandas
    Args:
        filepath (str): Path to CSV file
    Returns:
        pandas.DataFrame: Loaded dataframe
    """
    pass

def handle_missing_values(df):
    cleaned_df=df['Age'].isna().sum()==0
    cleaned_df=df['Salary'].isna().sum()==0
    return(handle_missing_values)
    """
    Handle missing values in the DataFrame
    1. Identify number of missing values
    2. Fill missing values with appropriate method
    Returns:
        pandas.DataFrame: Cleaned dataframe
    """
    pass

def select_data(df):
    selected_df=df['Name','Age','Salary']
    selected_df=pd.DataFrame(selected_df)
    return(select_data)
    """
    Select specific columns and rows from DataFrame
    Returns:
        pandas.DataFrame: Selected data
    """
    pass

def rename_columns(df):
    renamed_df=select_data['name','age','salary']
    return(rename_columns)
    """
    Rename columns of the DataFrame
    Returns:
        pandas.DataFrame: DataFrame with renamed columns
    """
    pass
