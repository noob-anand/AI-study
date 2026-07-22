import pandas as pd

#series using dictionary

print()

data={"1":100, "2":200, "3":300, "4":400, "5":500}

a=pd.Series(data)

print(a)
print()

print(a['2'])
print()

a['2'] +=250
print(a)
print()

print(a[a>300])
print()