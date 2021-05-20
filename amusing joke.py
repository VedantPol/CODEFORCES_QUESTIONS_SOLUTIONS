a=input()
b=input()
a=a+b
b=[]
for x in a:
    b.append(x)
c=input()
d=[]
for x in c:
   d.append(x)
b.sort()
d.sort()
if b==d:
    print("YES")
else:
    print("NO")