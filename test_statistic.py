from abc import abstractmethod


class TestStatistic:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        return self.test_statistic(*args, **kwargs)

    @abstractmethod
    def test_statistic(self, data):
        pass


class DiffMeans(TestStatistic):
    def __init__(self, direction=None):
        super().__init__()
        self.direction = direction

    def test_statistic(self, data):
        group1, group2 = data
        if self.direction is None or self.direction == "both":
            test_stat = abs(group1.mean() - group2.mean())
        elif self.direction == "right":
            test_stat = group1.mean() - group2.mean()
        elif self.direction == "left":
            test_stat = group2.mean() - group1.mean()
        else:
            raise ValueError("direction must be either right or left")
        return test_stat


class DiffProps(DiffMeans):
    pass


class Props(TestStatistic):
    def __init__(self):
        pass

    def test_statistic(self, data):
        return data.mean()
