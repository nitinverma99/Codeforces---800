for cases in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    if lst.count(1) == 0 or lst.count(1) == 1:
        print('0')
    else:
        index1 = lst.index(1)
        gst = lst[::-1]
        index2 = gst.index(1)
        index2 = n- index2 - 1
        print(index2 - index1 - lst.count(1) + 1)