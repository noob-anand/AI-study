import numpy as np

#Q1
data = np.loadtxt(
    r'E:\code\AI study\Numpy\numpy code\wind stastics\wind.data'
)

print(data.shape)
print()

#Q2
a = data[:, 3:]
print(a.shape)
print()

print(a.max()) 
print()
print(a.min()) 
print()
print(a.mean()) 
print()
print(a.std()) 
print()

#Q3
print(a.max(axis=0)) 
print()
print(a.min(axis=0)) 
print()
print(a.mean(axis=0)) 
print()
print(a.std(axis=0)) 
print()

#Q4
print(a.max(axis=1)) 
print()
print(a.min(axis=1)) 
print()
print(a.mean(axis=1)) 
print()
print(a.std(axis=1)) 
print()

#Q5
print(np.argmax(a,axis=1)+4) #column index of max value in each row
print()

#Q6
b=np.array(data[:, 0:3])
r,c=np.unravel_index(np.argmax(a), a.shape) 
print('6. Day of maximum reading')
print('  Year:', int(b[r, 0]))
print('  Month:', int(b[r, 1]))
print('  Day:', int(b[r, 2]))
print()

#Q7
c=np.array(b[:,1]==1) #boolean array for month of January
d=np.array(a[c]) #wind data for January
print(d.mean(axis=0)) 
print()

