a=int(input())
for x in range(0,a):
    b=int(input())
    if b%2==0:
        if b>2:
            print((b//2)-1)
        else:
            print("0")
    elif b%2!=0:
        if b>2:
            print(b//2)
        else:
            print("0")