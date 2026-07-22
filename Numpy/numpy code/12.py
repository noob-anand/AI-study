import numpy as np

a=np.array([-1,2,5,5])

print(a==a.max()) #returns true at max postion
print()

print(a[a==a.max()]) #returns max value
print()

print(np.where(a==a.max())) #returns index of max value
print()

