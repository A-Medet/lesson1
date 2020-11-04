s = input(134)
l = len(s)
i = 0
max_num = 0
while i <= l:
    n = int(s[i])
    if max_num < n:
        max_num = n
    i += 1

print(max_num)

