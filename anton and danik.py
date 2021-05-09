a=int(input())
b=input()
anton=danik=0
for x in range(0,a):
    if b[x]=="A":
        anton=anton+1
    elif b[x]=="D":
        danik = danik+1
if anton>danik:
    print("Anton")
elif danik>anton:
    print("Danik")
else:
    print("Friendship")