a, b = map(int, input().split())
count=0
while(a<=b):
    a = a*3
    b = b*2
    count += 1
    if a <= b:
        continue
    else:
        print(count)
        break