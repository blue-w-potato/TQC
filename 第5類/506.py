a,b,c = int(input()),int(input()),int(input())
def compute(a,b,c):
    d = b**2-4*a*c
    if d<0:
        return False
    if d == 0:
        return [(-b)/(2*a)]
    return [(-b+d**0.5)/(2*a), (-b-d**0.5)/(2*a)]
a = compute(a,b,c)
if a:
    if len(a) == 1:
        print(a[0])
    else:
        a,b = a
        print( f'{a}, {b}' )
else:
    print("Your equation has no root.")
