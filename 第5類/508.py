def compute( x, y ):
    for i in range(min((x,y)), 0, -1):
        if x%i==0 and y%i==0:
            return i
x,y = map(int,input().split(','))
print(compute(x,y))