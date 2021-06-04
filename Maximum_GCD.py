# for i in range(int(input())):
#     k = int(input())
#     lst= []
#     for i in range(1, k+1):
#         for j in range(1, k+1):
#             if i == j:
#                 continue
#             else:
#                 if i<j:
#                     for l in range(i, 0, -1):
#                         if i%l == 0 and j%l == 0:
#                             lst.append(l)
#                             break
#                 else:
#                     for l in range(j, 0, -1):
#                         if i%l == 0 and j%l == 0:
#                             lst.append(l)
#                             break
#     print(max(lst))
for i in range(int(input())):
    k = int(input())
    if k%2 == 0:
        print(k//2)
    else:
        print((k-1)//2)