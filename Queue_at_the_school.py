n, time = map(int, input().split())
string = input()
string = list(string)
for i in range(time):
    j =0 
    while j < n-1 :
        if string[j] =='B' and string[j+1] == 'G':
            string[j] = 'G'
            string[j+1] = 'B'
            j += 1
        j += 1
print("".join(string))
 