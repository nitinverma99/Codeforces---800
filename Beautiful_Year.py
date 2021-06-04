year = int(input())
while(True):
    year = year+1
    k = set(str(year))
    if len(k) == 4:
        print(year)
        break 
