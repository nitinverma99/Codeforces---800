gst = []
for cases in range(int(input())):
    k = input()
    gst.append(k)
for i in range(len(gst)):
    l = gst[i]
    if l.startswith('OO'):
        gst[i] = '++'+ l[2:]
        print("YES")
        print(*gst, sep="\n")
        break
    elif l.endswith('OO'):
        gst[i] = l[:3] + '++'
        print("YES")
        print(*gst, sep="\n")
        break
    elif i== len(gst)-1:
        print("NO")
        break
    else:
        continue
