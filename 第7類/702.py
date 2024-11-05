a = ()
for i in range(2):
    print(f'Create tuple{i+1}:')
    while True:
        n = int(input())
        if n == -9999:break
        a += (n,)
print('Combined tuple before sorting:',a)
print('Combined list after sorting:',sorted(a))
