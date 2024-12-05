s = 0
for i in input():
    print(f'ASCII code for \'{i}\' is {ord(i)}')
    s+=ord(i)
print(s)