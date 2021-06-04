guest = list(input())
host = list(input())
pile = list(input())
total_list = [*guest, *host]
if len(total_list) == len(pile):
    for i in pile:
        if i in total_list:
            total_list.remove(i)
        else:
            print("NO")
            break

    if len(total_list) == 0:
        print("YES")
else:
    print("NO")
    