import numpy as np

a = np.arange(6).reshape(2, 3)
print(a)
print()

print(a.sum())
print()

print(a.sum(axis=0)) #see axis from axis chart pg 19 (vertical sum)
print()

print(a.sum(axis=1)) #(horizontal sum)
