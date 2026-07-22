import numpy as np

rng = np.random.default_rng()

fruits = np.array(['🍎', '🍌', '🍒', '🌴', '🍇'])
fruit = rng.choice(fruits)

print(fruit)