import pytest
import pandas as pd
import numpy as np
from scipy import stats

from hypothesis import Hypothesis
from generator import Permute
from test_statistic import DiffProps


@pytest.fixture
def data():
    offshore = pd.read_csv("https://moderndive.com/data/offshore.csv")
    return offshore


def test_two_proportions_pvalue(data):
    contingency = data.pivot_table(
        index="response", columns="college_grad", aggfunc="size"
    )
    _, p, _, _ = stats.chi2_contingency(contingency, correction=False)

    yes = (
        data.query('college_grad == "yes"')["response"].values == "no opinion"
    )
    no = data.query('college_grad == "no"')["response"].values == "no opinion"

    hypo = Hypothesis(
        (yes, no), generator=Permute(), test_statistic=DiffProps()
    )

    hypo.simulate()
    np.testing.assert_almost_equal(hypo.PValue, p, decimal=2)
