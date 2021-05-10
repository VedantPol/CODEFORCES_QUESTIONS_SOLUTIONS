x=int(input())
ac=0
for a in range(0,x):
    u=input()
    u=u.split(" ")
    if (int(u[1])-int(u[0]))>=2:
        ac=ac+1

print(ac)