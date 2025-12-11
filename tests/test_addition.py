import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from EO_processing import additions

def test_add_years_basic():
    df = pd.DataFrame({"signing_date": ["2020-01-15", "1994-07-01"]})
    out = additions.add_years(df.copy(), "signing_date")
    assert list(out["year"]) == ["2020", "1994"]

def test_add_months_basic():
    df = pd.DataFrame({"signing_date": ["2020-01-15", "1994-12-01"]})
    out = additions.add_months(df.copy(), "signing_date")
    assert list(out["month"]) == ["01", "12"]

def test_add_publication_delay_basic():
    df = pd.DataFrame({
        "signing_date": ["2020-01-01", "2020-01-10"],
        "publication_date": ["2020-01-06", "2020-01-10"]
    })
    out = additions.add_publication_delay(df.copy())
    # 2020-01-06 - 2020-01-01 = 5 days
    assert list(out["days_diff"]) == [5, 0]


def test_add_publication_delay_invalid_dates():
    df = pd.DataFrame({
        "signing_date": ["not_a_date"],
        "publication_date": ["2020-01-06"]
    })
    out = additions.add_publication_delay(df.copy())
    assert pd.isna(out["days_diff"].iloc[0])



def test_add_revoked_flag_and_amends_flag():
    df = pd.DataFrame({
        "disposition_notes": [
            "Revoked by: EO 14016",
            "Amends: EO 13597",
            None,
            "Some other text"
        ]
    })
    out = additions.add_revoked_flag(df.copy())
    out = additions.add_amends_flag(out)

    assert list(out["is_revoked"]) == [True, False, False, False]
    assert list(out["is_amendment"]) == [False, True, False, False]