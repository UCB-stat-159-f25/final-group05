import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from EO_processing import verify

def test_verify_type_all_correct():
    df = pd.DataFrame({
        "type": ["Presidential Document", "Presidential Document"]
    })
    count = verify.verify_type(df, "Presidential Document")
    assert count == 0


def test_verify_type_some_incorrect():
    df = pd.DataFrame({
        "type": ["Presidential Document", "Other", "Other"]
    })
    count = verify.verify_type(df, "Presidential Document")
    assert count == 2


def test_fix_type_filters_correctly():
    df = pd.DataFrame({
        "type": ["Presidential Document", "Other", "Presidential Document"],
        "value": [1, 2, 3]
    })
    new_df = verify.fix_type(df, "Presidential Document")
    assert len(new_df) == 2
    assert list(new_df["value"]) == [1, 3]


def test_verify_subtype_and_fix_subtype():
    df = pd.DataFrame({
        "subtype": ["Executive Order", "Other", "Executive Order"],
        "value": [10, 20, 30]
    })
    count = verify.verify_subtype(df, "Executive Order")
    assert count == 1

    new_df = verify.fix_subtype(df, "Executive Order")
    assert len(new_df) == 2
    assert list(new_df["value"]) == [10, 30]