n = int(input())
for i in range(n):
    no = int(input())
    moves= 0
    lst = list(map(int, input().split()))
    gst = list(map(int, input().split()))
    min1 = min(lst)
    min2 = min(gst)
    for i in range(no):
        count1 = 0
        count2 = 0
        if lst[i] > min1:
            count1 = lst[i] - min1
        if gst[i] > min2:
            count2 = gst[i] - min2
        moves += max(count1, count2)
    print(moves)