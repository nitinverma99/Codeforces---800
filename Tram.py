n = int(input())
lst = []
total = 0
for i in range(n):
    a, b = map(int, input().split())
    total = total - a + b
    lst.append(total)
print(max(lst))