inp = input()
l = 0
u = 0
for i in range(len(inp)):
    if inp[i].isupper():
        u += 1
    else:
        l += 1
if l == u or l>u :
    print(inp.lower())
else:
    print(inp.upper())