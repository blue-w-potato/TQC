w = input()
e = input()
r = input()
with open(w,'r') as s:
    a = s.read()
    print('=== Before the replacement')
    print(a)
print('=== After the replacement')
print(a.replace(e,r))