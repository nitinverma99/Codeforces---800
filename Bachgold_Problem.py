n = int(input())
count= 0
if n%2 == 0:
    count = n//2
    print(count)
    print(count * '2 ')
else:
    count = (n-1)//2
    print(count)
    print((count-1)*'2 ' + '3')