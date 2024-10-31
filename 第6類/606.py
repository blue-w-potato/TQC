def compute(r,c):
    for i in range(r):
        for j in range(c):
            print(f'{j-i:4}',end='')
        print()

r = int(input())
c = int(input())
compute(r,c)