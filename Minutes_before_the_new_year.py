for i in range(int(input())):
    h, m = list(map(int, input().split()))
    hours_to_minutes = (23-h)*60
    minutes = (59-m)
    print(hours_to_minutes + minutes+1)