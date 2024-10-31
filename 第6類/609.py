a = []
for w in range(2):
    print(f'Enter matrix {w+1}:')
    a.append([])
    a[-1].append(int(input('[1, 1]: ')))
    a[-1].append(int(input('[1, 2]: ')))
    a[-1].append(int(input('[2, 1]: ')))
    a[-1].append(int(input('[2, 2]: ')))

for w in range(2):
    print(f'Matrix {w+1}:')
    print(*a[w][:2],end=' ')
    print()
    print(*a[w][2:],end=' ')
    print()

a = [a[0][i]+a[1][i] for i in range(4)]
print(f'Sum of 2 matrices:')
print(*a[:2],end=' ')
print()
print(*a[2:],end=' ')
