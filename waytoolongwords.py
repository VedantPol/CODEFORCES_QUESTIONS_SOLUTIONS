j=int(input())
for n in range(0,j):
    a=str(input())
    if len(a)>10:
        x=a[0]
        y=a[-1]
        u=str(len(a)-2)
        print(x+u+y)
    else:
        print(a)


