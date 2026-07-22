import pandas as pd

#series using series

print()

a=pd.Series([ 1, 2.3, 3,4, 5.67 ])

print(a)
print()

b=pd.Series([ 1, False, 3, 'c', '5.67' ])

print(b)
print()

data=[101,102,103,200,202]
c=pd.Series(data,index=['a','b','c','d','e'])
print(c)
print()

print(c['a'])
print()

c['a']=100
print(c)
print()

print(c[c>=200])
print()

