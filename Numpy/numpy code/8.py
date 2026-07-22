import numpy as np

# making 2-D arr of 36 elements with 6 rows and 6 columns
a = np.arange(36).reshape(6, 6)
print(a)
print()

print(a[[0, 1, 2, 3, 4],
[1, 2, 3, 4, 5]])
print()

print(a[3:, [0, 2, 5]])
print()

mask = np.array(
[1, 0, 1, 0, 0, 1],
dtype=bool)
print(a[mask, 2])
print()