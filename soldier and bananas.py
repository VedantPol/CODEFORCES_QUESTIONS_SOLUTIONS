k,n,w=[int(i) for i in input().split(" ")]
total=0
for a in range(w+1):
    total=(a*k)+total

if n>=total:
    print("0")
elif n<total:
    total=total-n
    print(total)


