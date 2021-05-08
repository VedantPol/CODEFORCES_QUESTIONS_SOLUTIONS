a=int(input())
tram=0
lol=0
for q in range(a):
    c=[int(i) for i in input().split(" ")]
    tram=tram-c[0]
    if lol<=tram:

        lol=tram
    tram=tram+c[1]
    if lol<=tram:

        lol=tram

print(lol)

