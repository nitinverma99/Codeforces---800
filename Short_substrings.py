n = int(input())
for i in range(n):
    k = list(input())
    lst = []
    i=0
    while(i<len(k)):
        if i == 0:
            lst.append(k[i])
            i+=1
        elif i==len(k)-1:
            lst.append(k[i])
            break
        else:
            if k[i+1] == k[i]:
                lst.append(k[i])
                i += 2
            else:
                lst.append(k[i])
                i += 1
    c = ''.join(lst)
    print(c)
                
