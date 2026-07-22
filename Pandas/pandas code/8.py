import pandas as pd

# Aggegration

a=pd.read_csv("E:\code\AI study\Pandas\pandas code\data.csv",index_col="ID")
print()

# print(a.mean())
# will give error bcs there are columns with no numeric value

print(a.mean(numeric_only=True))
print()
# will work for column with numeric value only
# same for sun,min,max,

print(a.count())
print()
# gives total values in each column

print(a["HP"].mean())
print()

print(a["HP"].count())
print()

gp=a.groupby("Type1")

print(gp["HP"].mean())