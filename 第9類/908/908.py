w = input()
e = int(input())
with open(w, 'r') as s:
    a = []
    for i in s.read().split():
        a += i.split()
print('\n'.join(sorted( [ i for i in set(a) if a.count(i) == e ] )))