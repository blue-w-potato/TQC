a = []
for i,k in enumerate((5,3,9)):
    print(f'Input to set{i+1}:')
    a.append(set())
    for j in range(k):
        a[-1].add(int(input()))
print('set2 is subset of set1:', len(a[1]&a[0]) == len(a[1]))
print('set3 is superset of set1:', len(a[2]&a[0]) == len(a[0]))