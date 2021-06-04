n = input()
n4 = n.count("4")
n7 = n.count("7")
ssum = str(n4 + n7)
ssum4 = ssum.count("4")
ssum7 = ssum.count("7")
total = ssum4 +ssum7
if total == len(ssum):
    print('YES')
else:
    print('NO')