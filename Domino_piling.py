a, b= map(int, input().split(' '))
total_squares = a*b
if total_squares % 2 ==0:
    print(int(total_squares/2))
else:
    print(int((total_squares - 1)/2))