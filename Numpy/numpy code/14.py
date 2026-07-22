import numpy as np

a = np.arange(6).reshape(2, 3)
print(a)
print()

b=a.reshape(3, 2) 
print(b)
print()

c=a.flatten() 
print(c)
print()

d=a.ravel() 
print(d)
print()