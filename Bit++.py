x = 0
for i  in range(int(input())):
    oper = input()
    if (oper == 'X++' or oper == '++X'):
        x += 1 
    else:
        x -= 1
print(x)