print('=== Before the deletion')

w = input()
with open(w, 'r') as s:
    a = s.read()
    print(a)

print('=== After the deletion')
a = a.replace(input(),'')

with open(w, 'wt') as s:
    print(a,end='',file=s)
print(a)