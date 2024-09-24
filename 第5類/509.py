x,y = map(int,input().split(','))
m,n = map(int,input().split(','))

def compute(x,y,m,n):
    a = x*n + m*y
    b = y*n
    while True:
        if a%b == 0:
            a//=b
            b = 'yee'
            break
        if b%a == 0:
            b//=a
            a = 1
            break
        t = 0
        for i in range(min((a,b)), 0, -1):
            if i == 1:
                t+=1
                break
            if a%i == 0 and b%i == 0:
                a//=i
                b//=i
                break
        if t:break
    if b == 'yee':
        return f'{x}/{y} + {m}/{n} = {a}'
    else:
        return f'{x}/{y} + {m}/{n} = {a}/{b}'
print(compute(x,y,m,n))