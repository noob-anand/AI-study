import numpy as np

#Random INT generation

rng = np.random.default_rng()

print(rng.integers(low=1, high=101))
print()

print(rng.integers(low=1, high=101,size=3))
print()

print(rng.integers(low=1, high=101,size=(2,3)))
print()