x=input()
x=x.split(" ")
p=int(x[1])
y=input()
y=y.split(" ")
w=0

for a in range(0,int(x[0])):
    if int(y[a])>p:
        w=w+2
    else:
        w=w+1


print(w)