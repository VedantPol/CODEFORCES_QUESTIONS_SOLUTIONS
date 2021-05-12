a=input()
b=input()
c=len(a)
d=""
for x in range(0,c):
    if a[x]==b[x]:
        d=d+"0"
    else:
        d=d+"1"
print(d)