def compute(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return []
    if d == 0:
        return [-b/2/a]
    return sorted([(-b-d**0.5)/2/a, (-b+d**0.5)/2/a], reverse=True)
a,b,c = int(input()), int(input()), int(input())
k = compute(a,b,c)
if k:
    print(k[0], end='')
    if len(k)>1: print(',',k[1])
else:
    print("Your equation has no root.")