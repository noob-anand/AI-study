import pandas as pd

#DataFrames using dictionary

print()

data={"Name":['spogebob','patrick','squid'],
      "Age":[20,21,22]
      }

a=pd.DataFrame(data, index=['1','2','3'])

print(a)
print()

print(a.loc['1'])
print()

print(a.loc['3'])
print()

#add new column

a['Job']=['Cook','N/A','Cashier']

print(a)
print()

#add a new rows
r=pd.DataFrame([{"Name":'Sandy',"Age":28,"Job":"Builder"},
                {"Name":'Soggy',"Age":38,"Job":"Manager"}
                ],
               index=['4','5']
               )
print(r)
print()

a=pd.concat([a,r])

print(a)
print()