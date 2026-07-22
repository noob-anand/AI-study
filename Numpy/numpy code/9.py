import numpy as np

# making 2-D arr of 25 elements with 5 rows and 5 columns
a = np.arange(25).reshape(5, 5)
print(a)
print()

# blue elements
print(a[[0,2,3,3],[2,3,1,4]])
print()

# numbers divisible by 3
mask = a % 3 == 0
print(mask)
print()

print(a[mask])
print()
