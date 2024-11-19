a = {}
while True:
    key = input('Key: ')
    if key == 'end':break
    a[key] = input('Value: ')
for i in sorted(a.keys()):
    print(i+':', a[i])