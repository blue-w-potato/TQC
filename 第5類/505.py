def compute(a, x,y):
    for i in range(y):
        for j in range(x):
            print(a,end=' ')
        print()

compute(input(), int(input()), int(input()))