def compute(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    f = [0, 1]
    print('0 1 ',end='')
    for i in range(2, n):
        f.append(f[-1]+f[-2])
        print(f[-1],end=' ')

n = int(input())
compute(n)