# slicing

import numpy as np

#  IMP
#  a[lower:upper:step]

a=np.array([1,2,3,4,5,6,7,8])
print(a[0:4])
print(a[:4])
print()

print(a[1:3])
print()

print(a[0:8:2])
print(a[::2])
print()


#  0  1  2  3  4  5  6  7
# -8 -7 -6 -5 -4 -3 -2 -1

print(a[0:-2])

# 2-D array slicing in NOTES