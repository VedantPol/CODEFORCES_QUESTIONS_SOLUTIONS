x=int(input())
br=0
for i in range(0,x):
    y=str(input())
    a=y.split(" ")
    yes = 0
    for b in a:
        if int(b)>0:
            yes=yes+1

    if yes>=2:
        br=br+1

print(br)