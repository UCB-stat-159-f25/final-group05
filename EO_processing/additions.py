import pandas as pd

def add_years(df, col_to_use):
    df['year'] = df[col_to_use].str[:4]
    return df

def add_months(df, col_to_use):
    df['month'] = df[col_to_use].str[5:7]
    return df

def add_publication_delay(df, signing_col="signing_date", publication_col="publication_date",
                          output_col="days_diff"):
    """
    Add a column with the difference in days between signing and publication dates.
    """
    signed = pd.to_datetime(df[signing_col], errors="coerce")
    published = pd.to_datetime(df[publication_col], errors="coerce")
    df[output_col] = (published - signed).dt.days
    return df

def add_revoked_flag(df, disposition_col="disposition_notes", output_col="is_revoked"):
    """
    Add a boolean column indicating whether an executive order has been revoked.
    """
    df[output_col] = df[disposition_col].fillna("").str.contains("Revoked", case=False)
    return df


def add_amends_flag(df, disposition_col="disposition_notes", output_col="is_amendment"):
    """
    Add a boolean column indicating whether an executive order amends another EO.
    """
    df[output_col] = df[disposition_col].fillna("").str.contains("Amends", case=False)
    return df

