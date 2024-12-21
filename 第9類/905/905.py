w = input()
e = input()

with open(w,'r') as s:
    a = s.read()
    
print('=== Before the deletion')
print(a)
a = a.replace(e,'')

# 不用寫入
# with open(w,'wt') as s:
#     print(a, end='', file=s)
    
    
print('=== After the deletion')
print(a)