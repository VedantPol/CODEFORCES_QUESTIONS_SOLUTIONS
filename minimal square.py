a=int(input())
for x in range(a):
    b,c=[int(p)for p in input().split(" ")]
    d=min(b,c)
    e=max(b,c)
    if 2*d>=e:
        d=d*2
        print(d * d)
    else:
        print(e*e)