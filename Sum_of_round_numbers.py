n = int(input())
for i in range(n):
    k = input()
    k = list(k)
    lst = []
    for i in range(len(k)):
        if k[i] == '0' :
            continue
        else:
            lst.append(k[i] + str('0'*(len(k)-1-i)))
    print(len(k)-k.count('0'))
    print(*lst, sep=" ")