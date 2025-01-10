print('=== Before the replacement')
w = input()
with open(w,'r') as s:
    a = s.read()
    print(a)

print('=== After the replacement')
a = a.replace(input(),input())
print(a)

with open(w,'wt') as s:
    print(a,end='',file=w)