import pandas as pd

def verify_type(df, desired):
    count_incorrect = 0
    for _, row in df.iterrows():
        if row['type'] == desired:
            continue
        else:
            count_incorrect += 1
    return count_incorrect
    
def fix_type(df, desired):
    new_df = pd.DataFrame()
    for _, row in df.iterrows():
        if row['type'] == desired:
            new_df.loc[len(new_df)] = row
    return new_df
    
def verify_subtype(df, desired):
    count_incorrect = 0
    for _, row in df.iterrows():
        if row['subtype'] == desired:
            continue
        else:
            count_incorrect += 1
    return count_incorrect

def fix_subtype(df, desired):
    new_df = pd.DataFrame()
    for _, row in df.iterrows():
        if row['subtype'] == desired:
            new_df.loc[len(new_df)] = row
    return new_df