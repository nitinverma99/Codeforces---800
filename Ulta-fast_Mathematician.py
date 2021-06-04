a = input()
b = input()
lst = []
for i in range(len(a)):
    if a[i] == b[i]:
        lst.append('0')
    else:
        lst.append('1')
print(''.join(lst))