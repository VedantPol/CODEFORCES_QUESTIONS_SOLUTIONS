a=input().split(" ")
b="#"
e="."
cout=0
c=int(a[0])
d=int(a[1])
for x in range(1,c+1):
    if x%2==1:
        print(b*d)
    elif x%2==0:
        cout+=1
        if cout%2==1:
            print(e * (d - 1), end="")
            print("#")
        elif cout%2==0 :
            print("#",end="")
            print(e * (d - 1))
