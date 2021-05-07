b=input().split(" ")
l=int(b[0])

for a in range(0,int(b[1])):
    p=l%10
    if p==0:
        l=l/10
    else :
        l=l-1
print(int(l))

