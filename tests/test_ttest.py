import pytest
import pandas as pd
import numpy as np
from scipy import stats

from hypothesis import Hypothesis
from generator import Permute
from test_statistic import DiffMeans
from specifier import Specifier


@pytest.fixture
def data():
    data = (
        pd.read_table("https://moderndive.com/data/cleSac.txt")
        .rename(
            columns={
                "Metropolitan_area_Detailed": "metro_area",
                "Total_personal_income": "income",
            }
        )
        .dropna()
    )

    return data


def test_ttest_pvalue(data):
    OH = data.loc[
        lambda df: df["metro_area"] == "Cleveland_ OH", "income"
    ].values
    CA = data.loc[
        lambda df: df["metro_area"] == "Sacramento_ CA", "income"
    ].values

    _, p = stats.ttest_ind(OH, CA)

    hypo = Hypothesis(
        data,
        specifier=Specifier(response="income", explanatory="metro_area"),
        generator=Permute(),
        test_statistic=DiffMeans(),
    )

    hypo.simulate()
    np.testing.assert_almost_equal(hypo.PValue, p, decimal=2)
