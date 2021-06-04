k,n,w = map(int, input().split(' '))
total_cost = 0
for i in range(w):
    total_cost += (i+1) * k

if total_cost > n:
    print(total_cost - n)
else:
    print("0")