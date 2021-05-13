a=input()
a=a[1:-1]
if a=="":
    pass
else:
    a=a.split(", ")
b=[]
for x in a:
    if x not in b:
        b.append(x)
print(len(b))