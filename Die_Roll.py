y,w = list(map(int, input().split()))
total = 6
maxx = max([y,w])
left = total -maxx +1
if left == 1:
    print('1/6')
else:
    if left == 2:
        print('1/3')
    elif left == 3:
        print('1/2')
    elif left == 4:
        print('2/3')
    elif left == 5:
        print('5/6')
    elif left == 6:
        print('1/1')