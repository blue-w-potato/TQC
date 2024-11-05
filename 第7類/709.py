a = []
while True:
    k = input('Key: ')
    if k == 'end':break
    a.append(k)
    input('Value: ')
s = input('Search key: ')
print(s in a)