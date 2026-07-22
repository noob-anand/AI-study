#Fancy indexing
import numpy as np
a = np.arange(0, 80, 10)
indices = [1, 2, -3]
y = a[indices]
print(y)


b=np.array([-1,-3,1,4,-6,9,3])
mask=np.array([True,True,False,False,True,False,False])
z=b[mask]
print(z)

# turn negative values to 0
b[mask]=0
print(b)