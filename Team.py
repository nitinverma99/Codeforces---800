i = int(input())
count = 0
for i in range(i):
    n = list(map(int, input().split(' ')))
    if sum(n) == 2 or sum(n) == 3 :
        count +=1
print(count)  
