import pandas as pd

# Data Cleaning

a=pd.read_csv("E:\code\AI study\Pandas\pandas code\data.csv",index_col="ID")
print()


b=a.drop(columns=["HP","Attack"])

print(b.to_string())
print()

# to replace any value
a["Type2"]=a["Type2"].replace({" ":"NA"})

c=a.drop_duplicates()

print(c)
print()