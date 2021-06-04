n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a == b :
        print('0')
        continue
    else:
        count = 0
        diff = abs(b-a)
        for i in range(10, 0, -1):
            if (diff)/i >= 1:
                count += diff//i
                diff = diff%i
        print(count)
