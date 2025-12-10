import pandas as pd

def add_years(df, col_to_use):
    df['year'] = df[col_to_use].str[:4]
    return df

def add_months(df, col_to_use):
    df['month'] = df[col_to_use].str[5:7]
    return df