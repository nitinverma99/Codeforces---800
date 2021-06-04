n = int(input())
string = input().lower()
settt = set(string)
if len(settt) == 26:
    print("YES")
else:
    print("NO")