a= int(input())
c=0
for x in range(a):
    b=input()
    if b=="Tetrahedron":
        c+=4
    elif b=="Cube":
        c+=6
    elif b=="Octahedron":
        c+=8
    elif b=="Dodecahedron":
        c+=12
    elif b=="Icosahedron":
        c+=20

print(c)        