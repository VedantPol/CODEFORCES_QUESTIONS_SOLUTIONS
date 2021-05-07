a=input()
de=[]
for f in a:
    de.append(f)
res=[]
for i in de:
    if i not in res:
        res.append(i)

b=len(res)

if b%2==0:
    print("CHAT WITH HER!")
elif b%2!=0:
    print("IGNORE HIM!")