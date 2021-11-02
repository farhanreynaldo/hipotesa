class Hypothesis:
    def __init__(self, data, specifier, generator, test_statistic, iters=1000):
        self.data = data
        self.specifier = specifier
        self.generator = generator
        self.test_statistic = test_statistic
        self.iters = iters
        self.is_simulated = False

    def simulate(self):
        self._data = self.specifier.transform(self.data)
        self.test_stats = [
            self.test_statistic(self.generator(self._data))
            for _ in range(self.iters)
        ]
        self.is_simulated = True
        return self

    @property
    def PValue(self):
        if not self.is_simulated:
            raise Exception("Simulation not performed")
        self.actual = self.test_statistic(self._data)
        return sum(self.test_stats >= self.actual) / len(self.test_stats)
