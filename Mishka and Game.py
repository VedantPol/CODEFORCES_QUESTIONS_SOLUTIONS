a=int(input())
Mika=0
Chris=0
for x in range(a):
    b,c=[int(item) for item in input().split(" ")]
    if b>c:
        Mika+=1
    elif c>b:
        Chris+=1
if Mika>Chris:
    print("Mishka")
elif Chris>Mika:
    print("Chris")
else:
    print("Friendship is magic!^^")
