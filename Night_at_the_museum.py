s = list(input())
count = 0
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
first = 'a'
for i in range(len(s)):
    then = s[i]
    value = lst.index(then) - lst.index(first)
    if abs(value) < (26 - abs(value)):
        count += abs(value)
    else:
        count += (26 - abs(value))
    first = s[i]
print(count)