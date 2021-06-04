n = list(input())
lst = input().split(' ')
gst = []
for i in range(5):
    gst.append(lst[i][1])
for i in range(5):
    lst[i] = lst[i][0]
if n[0] in lst:
    print("YES")
elif n[1] in gst:
    print("YES")
else:
    print("NO")