import numpy as np

# Shuffle the array

rng = np.random.default_rng()

a=np.array([1,2,3,4,5])

rng.shuffle(a)

print(a)