import pandas as pd

# Filtering

a=pd.read_csv("E:\code\AI study\Pandas\pandas code\data.csv",index_col="ID")
print()

# only pokemon with hp 50 
hp=a[a["HP"]>50]

print(hp)
print()

water=a[(a["Type1"]=="Water") | (a["Type2"]=="Water")]

print(water)
print()

fireflying=a[(a["Type1"]=="Fire") & (a["Type2"]=="Flying")]

print(fireflying)