a=input()
p=len(a)
u=l=0
for z in range(0,p):
    if a[z].isupper():
        u=u+1
    elif a[z].islower():
        l=l+1
if u>l:
    a=a.upper()
    print(a)
elif l>=u:
    a=a.lower()
    print(a)
