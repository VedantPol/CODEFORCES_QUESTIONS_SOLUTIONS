a=input().split(" ")
b=[]
for x in a:
    if x not in b:
        b.append(x)
p=4-len(b)
print(p)