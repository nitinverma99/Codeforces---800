for i in range(int(input())):
    k = int(input())
    lst = list(map(int, input().split()))
    lst = set(lst)
    print(len(lst))