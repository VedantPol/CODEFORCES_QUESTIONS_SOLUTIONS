b=input().split(" ")
l=int(b[0])
b=int(b[1])
n=0
while b>=l:
    n=n+1
    l=l*3
    b=b*2
print(n)