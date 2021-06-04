n, k, l, c, d, p, nl, np = list(map(int, input().split()))
total_drink = k*l
slice = c*d
drinkss = total_drink/nl
saltt = p/np
minn = min([slice, drinkss, saltt])
print(int(minn//n))