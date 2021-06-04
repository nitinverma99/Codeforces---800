for cases in range(int(input())):
    n = int(input())
    s = input()
    count = 0
    for i in range(1,len(s)):
        if s[i] in s[:i] and s[i]!=s[i-1]:
            print("NO")
            count = 1
            break
        else:
            continue
    if count == 0:
        print("YES")
