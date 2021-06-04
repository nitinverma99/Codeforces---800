n, m = list(map(int, input().split()))
lst = []
for i in range(n):
    k = input().split(' ')
    lst.extend(k)
if 'C' in lst or 'M' in lst or 'Y' in lst:
    print('#Color')
else:
    print('#Black&White')