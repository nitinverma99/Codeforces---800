n = int(input())
lst = [1, 5, 10, 20, 100]
count = 0
for i in lst[::-1]:
    if i <= n:
        count += (n//i)
        n = n%i
print(count)