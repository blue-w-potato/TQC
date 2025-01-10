with open( 'data.txt', 'r') as s:
    a = s.read()
print('''Append completed!
Content of "data.txt":''')
a += '\n' + '\n'.join([input() for i in range(5)])
print(a)
with open('data.txt','wt') as s:
    print(a,end='',file=s)