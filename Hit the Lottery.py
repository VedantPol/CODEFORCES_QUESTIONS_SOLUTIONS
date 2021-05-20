a=int(input())
b=a//100
c=a%100
while c!=0:
    if c >= 20:
        c-=20
        b+=1
    elif c >= 10:
        c-=10
        b+=1
    elif c >= 5:
        c-=5
        b+=1
    elif c >= 1:
        c-=1
        b+=1
print(b)