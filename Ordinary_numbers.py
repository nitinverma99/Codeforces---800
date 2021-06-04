for i in range(int(input())):
    n = int(input())
    if n<10:
        print(n)
    else:
        k=str(n)
        count = 9
        for i in range(2, len(k)+1):
            for j in range(1,10):
                ele = '1' * i
                ele = int(ele)
                ele= ele*j
                if (ele)<=n:
                    count+=1
                else:
                    break
        print(count)