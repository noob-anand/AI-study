# 2-D array slicing question
import numpy as np

# making 2-D arr of 25 elements with 5 rows and 5 columns
a = np.arange(25).reshape(5, 5)
print(a)
print(a.shape)
print()
    

# RED
print('RED')
print(a[: ,1::2])
print()

# yellow
print('YELLOW')
print(a[4 , :])
print()

# blue
print('BLUE')
print(a[1::2, :3:2])