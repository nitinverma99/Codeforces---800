s = list(input())
gst = []
i = 0
while(i<len(s)) :
    if s[i] == '.':
        gst.append('0')
        i += 1
    elif s[i] == '-' and s[i+1] == '.':
        gst.append('1')
        i+= 2
    elif s[i] == '-' and s[i+1] == '-':
        gst.append('2')
        i+=2
    else:
        i+=1
        continue
print(''.join(gst))