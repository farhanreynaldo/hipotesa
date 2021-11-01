class TestStatistic:
    def __init__(self):
        pass


class DiffMeans(TestStatistic):
    def __init__(self):
        super().__init__()

    def __call__(self, data):
        group1, group2 = data
        test_stat = abs(group1.mean() - group2.mean())
        return test_stat
