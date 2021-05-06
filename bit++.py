x=0
d=0
p=int(input())
for a in range(0,p):
    b=input()
    if b=="++X":
        x = x + 1

    elif  b=="--X":
        x=x-1

    elif b == "X++":
        d=d+1

    elif b == "X--":
        d=d-1

x=x+d
print(x)