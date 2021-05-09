a=int(input())

f=False
while f==False:
    a += 1
    b=str(a)
    d=[]
    for x in b:
        if x  not in d:
            d.append(x)
    if len(d)==4:
        break

print(a)

