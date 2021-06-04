n = int(input())
lst = list(map(int, input().split()))
unseen = 0
recruited = 0
for i in range(n):
    if lst[i] <0 :
        unseen += 1
    else:break
for i in range(unseen,n):
    if lst[i] > 0:
        recruited += lst[i]
    elif lst[i] < 0:
        if recruited == 0:
            unseen += 1
        else:
            recruited -= 1
            
print(unseen)
