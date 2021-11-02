from pandas.api.types import is_numeric_dtype
import numpy as np


class Specifier:
    def __init__(self, response, explanatory=None, success=None):
        self.resp = response
        self.exp = explanatory
        self.success = success

    def transform(self, data):
        if self.exp is None:
            return (
                data[self.resp]
                if self.success is None
                else data[self.resp] == self.success
            )

        is_resp_numeric = is_numeric_dtype(data[self.resp])

        if is_resp_numeric:
            return data.groupby(self.exp)[self.resp].apply(np.array)
        elif not is_resp_numeric:
            if self.success is None:
                raise ValueError(
                    "Success should be defined for categorical column"
                )
            else:
                data = data.filter([self.resp, self.exp])
                data[self.resp] = data[self.resp] == self.success
                return data.groupby(self.exp)[self.resp].apply(np.array)
