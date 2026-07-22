import pandas as pd

a=pd.read_csv("E:\code\AI study\Pandas\pandas code\data.csv",index_col="ID")
print()

# Print by column

print(a["Name"])
print()

print(a[["Name","Type1"]].to_string())
print()

# Print by rows

print(a.loc[60])
print()

print(a.loc[60,["Name","Type1"]])
print()

print(a.loc[60:70,["Name","Type1"]])
print()