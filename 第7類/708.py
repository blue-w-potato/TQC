a = {}
for i in range(2):
    print(f'Create dict{i+1}:')
    while True:
        k = input('Key: ')
        if k == 'end':break
        a[k] = input('Value: ')
for i in sorted(a.keys()):
    print(f'{i}: {a[i]}')