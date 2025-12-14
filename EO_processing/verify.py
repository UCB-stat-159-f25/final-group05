import pandas as pd

def verify_type(df, desired):
    """
    Counting number of rows in dataframe where type column doesn't match desired input.
    Inputs (name : type -> purpose):
    df : pandas.DataFrame -> the dataframe being verified
    desired : any -> the expected value for the 'type' column of the given dataframe
    Output (type -> purpose):
    int -> count of the number of rows that do not match desired value in 'type' column
    """
    count_incorrect = 0
    for _, row in df.iterrows():
        if row['type'] == desired:
            continue
        else:
            count_incorrect += 1
    return count_incorrect
    
def fix_type(df, desired):
    """
    Returning dataframe with only rows where type column matches desired input.
    Inputs (name : type -> purpose):
    df : pandas.DataFrame -> the dataframe being modified
    desired : any -> the expected value for the 'type' column of the given dataframe
    Output (type -> purpose):
    pandas.DataFrame -> the dataframe with only the rows where type matches desired input.
    """
    new_df = pd.DataFrame()
    for _, row in df.iterrows():
        if row['type'] == desired:
            new_df.loc[len(new_df)] = row
    return new_df
    
def verify_subtype(df, desired):
    """
    Counting number of rows in dataframe where subtype column doesn't match desired input.
    Inputs (name : type -> purpose):
    df : pandas.DataFrame -> the dataframe being verified
    desired : any -> the expected value for the 'subtype' column of the given dataframe
    Output (type -> purpose):
    int -> count of the number of rows that do not match desired value in 'subtype' column
    """
    count_incorrect = 0
    for _, row in df.iterrows():
        if row['subtype'] == desired:
            continue
        else:
            count_incorrect += 1
    return count_incorrect

def fix_subtype(df, desired):
    """
    Returning dataframe with only rows where subtype column matches desired input.
    Inputs (name : type -> purpose):
    df : pandas.DataFrame -> the dataframe being modified
    desired : any -> the expected value for the 'subtype' column of the given dataframe
    Output (type -> purpose):
    pandas.DataFrame -> the dataframe with only the rows where subtype matches desired input.
    """
    new_df = pd.DataFrame()
    for _, row in df.iterrows():
        if row['subtype'] == desired:
            new_df.loc[len(new_df)] = row
    return new_df
