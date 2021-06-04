n = int(input())
for i in range(n):
    even = 0
    odd = 0
    no = int(input())
    lst = list(map(int, input().split()))
    for index,item in enumerate(lst):
        if item%2 == index%2:
            pass
        elif item%2 == 0:
            even += 1
        elif item%2 != 0:
            odd +=1
    if even == odd :
        print(even)
    else:
        print('-1')
            