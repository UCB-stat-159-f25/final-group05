import pandas as pd

def add_years(df, col_to_use):
    """
    Parsing column in given dataframe to add 'year' column.
    Inputs (name : type -> purpose):
    df : pandas.DataFrame -> the dataframe being modified
    col_to_use : any -> the expected value for the 'type' column of the given dataframe
    Output (type -> purpose):
    pandas.DataFrame -> input dataframe with added 'year' column
    """
    df['year'] = df[col_to_use].str[:4]
    return df

def add_months(df, col_to_use):
    """
    Parsing column in given dataframe to add 'month' column.
    Inputs (name : type -> purpose):
    df : pandas.DataFrame -> the dataframe being modified
    col_to_use : any -> the expected value for the 'type' column of the given dataframe
    Output (type -> purpose):
    pandas.DataFrame -> input dataframe with added 'month' column
    """
    df['month'] = df[col_to_use].str[5:7]
    return df

def add_publication_delay(df, signing_col="signing_date", publication_col="publication_date",
                          output_col="days_diff"):
    """
    Add a column with the difference in days between signing and publication dates.
    Inputs (name : type -> purpose):
    df : pandas.DataFrame -> the dataframe being modified
    signing_col : string -> the column name with the day an EO was signed  
    publication_col : string -> the column name with the day an EO was published  
    output_col : string -> the column name to add to the dataframe
    Output (type -> purpose):
    pandas.DataFrame -> input dataframe with added integer 'days_diff' column
    """
    signed = pd.to_datetime(df[signing_col], errors="coerce")
    published = pd.to_datetime(df[publication_col], errors="coerce")
    df[output_col] = (published - signed).dt.days
    return df

def add_revoked_flag(df, disposition_col="disposition_notes", output_col="is_revoked"):
    """
    Parsing column in given dataframe to add 'is_revoked' column.
    Inputs (name : type -> purpose):
    df : pandas.DataFrame -> the dataframe being modified
    disposition_col : string -> the column name to analyze/parse 
    output_col : string -> the column name to add to the dataframe
    Output (type -> purpose):
    pandas.DataFrame -> input dataframe with added boolean 'is_revoked' column.
    """
    df[output_col] = df[disposition_col].fillna("").str.contains("Revoked", case=False)
    return df


def add_amends_flag(df, disposition_col="disposition_notes", output_col="is_amendment"):
    """
    Parsing column in given dataframe to add 'is_amendment' column.
    Inputs (name : type -> purpose):
    df : pandas.DataFrame -> the dataframe being modified
    disposition_col : string -> the column name to analyze/parse 
    output_col : string -> the column name to add to the dataframe
    Output (type -> purpose):
    pandas.DataFrame -> input dataframe with added boolean 'is_amendment' column.
    """
    df[output_col] = df[disposition_col].fillna("").str.contains("Amends", case=False)
    return df

