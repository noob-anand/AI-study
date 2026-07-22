a=[1,2,3,4]
b=[5,6,7,8]
# what we get
c=a+b
print(c)
d=[]
# what we want
for first,second in zip(a,b): 
    d.append(first+second)
print(d) 