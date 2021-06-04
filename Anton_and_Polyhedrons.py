n = int(input())
count = 0 
for i in range(n):
    k = input()
    if k == "Tetrahedron":
        count += 4
    elif k == "Cube":
        count += 6
    elif k == "Octahedron":
        count += 8
    elif k == "Dodecahedron":
        count += 12
    elif k == "Icosahedron":
        count += 20
print(count)