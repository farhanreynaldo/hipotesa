import pytest
import pandas as pd
import numpy as np
from scipy import stats

from hypothesis import Hypothesis
from generator import Permute
from test_statistic import DiffMeans


@pytest.fixture
def data():
    cle_sac = (
        pd.read_table("https://moderndive.com/data/cleSac.txt")
        .rename(
            columns={
                "Metropolitan_area_Detailed": "metro_area",
                "Total_personal_income": "income",
            }
        )
        .dropna()
    )

    OH = cle_sac.loc[
        lambda df: df["metro_area"] == "Cleveland_ OH", "income"
    ].values
    CA = cle_sac.loc[
        lambda df: df["metro_area"] == "Sacramento_ CA", "income"
    ].values

    return OH, CA


def test_ttest_pvalue(data):
    OH, CA = data
    _, p = stats.ttest_ind(OH, CA)

    hypo = Hypothesis(
        (OH, CA), generator=Permute(), test_statistic=DiffMeans()
    )

    hypo.simulate()
    np.testing.assert_almost_equal(hypo.PValue, p, decimal=1)
