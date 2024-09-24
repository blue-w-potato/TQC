def compute(x):
    if x < 2:
        return 'Not Prime'
    k = [ True for i in range(int(x**0.5)+1) ]
    for i in range(2, len(k)):
        if k[i]:
            if x%i == 0:
                return 'Not Prime'
            for j in range(i**2, len(k),i):
                k[j] = False
    return 'Prime'

x = int(input())
print(compute(x))