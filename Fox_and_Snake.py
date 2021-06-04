a, b = map(int, input().split())
for i in range(1, a+1):
    if i%2 != 0 :
        print('#'*b)
    elif i%2 == 0 and i%4 != 0:
        print('.'*(b-1) + '#')
    elif i%2 == 0 and i%4 == 0:
        print('#' + '.'*(b-1))

    
