a = []
for k in 'XY':
    print(f'Enter group {k}\'s subjects:')
    a.append(set())
    while True:
        n = input()
        if n == 'end':break
        a[-1].add(n)

print(sorted((a[1]|a[0])))
print(sorted((a[1]&a[0])))
print(sorted((a[1]-a[0])))
print(sorted((a[1]|a[0])-(a[1]&a[0])))