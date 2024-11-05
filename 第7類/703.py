a = ()
while True:
    n = input()
    if n == 'end':break
    a += (n,)
print(a)
print(a[:3])
print(a[-3:])