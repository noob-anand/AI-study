import pandas as pd

a=pd.read_csv("E:\code\AI study\Pandas\pandas code\data.csv",index_col="ID")
print()

id=int(input("give id: "))

print(a.loc[id])