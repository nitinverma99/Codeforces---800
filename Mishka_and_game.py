n = int(input())
mishka = 0
chris = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    if a>b:
        mishka += 1
    elif b>a:
        chris += 1
if mishka>chris:
    print('Mishka')
elif chris>mishka:
    print('Chris')
else:
    print('Friendship is magic!^^')