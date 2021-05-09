a=input()
p=len(a)
luck=0
for x in range(0,p):
    if a[x]=="7" or a[x]=="4":
        luck=luck+1


if luck==4 or luck==7:
    print("YES")
elif luck==p:
    print("NO")
else:
    print("NO")


