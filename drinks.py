a=int(input())
c=input()
c=c.split(" ")
n=0
for q in range(a):
    n=n+int(c[q])

print((n/(a*100))*100)
