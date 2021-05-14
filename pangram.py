a=int(input())
b=input()
b=b.lower()
d=[]
for x in b:
    d.append(x)
c=[]
for x in d:
    if x not in c:
        c.append(x)
if len(c)!=26:
    print("NO")
else:
    print("YES")
