inp = input()
lst= []
for i in range(len(inp)):
    if inp[i] in lst:
        continue
    else:
        lst.append(inp[i])

if len(lst) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")