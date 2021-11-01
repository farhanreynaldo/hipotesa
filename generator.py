import numpy as np

rng = np.random.default_rng()


class Generator:
    def __init__(self):
        pass


class Permute(Generator):
    def __init__(self):
        super().__init__()

    def __call__(self, data):
        group1, group2 = data
        n, _ = len(group1), len(group2)
        pool = np.hstack((group1, group2))
        rng.shuffle(pool)
        return pool[:n], pool[n:]


class Bootstrap(Generator):
    def __init__(self):
        super().__init__()

    def __call__(self, data):
        raise NotImplementedError
