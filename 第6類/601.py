a = [int(input()) for i in range(12)]
for i in range(4):
    for j in range(3):
        print(f'{a[i*3+j]:3}',end='')
    print()
print(sum(a[0::2]))