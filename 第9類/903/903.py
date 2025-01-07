with open( 'data.txt', 'rt' ) as s:
    a = s.read()
for i in range(5):
    a += '\n' + input()

with open( 'test.txt', 'wt', encoding='utf-8' ) as s:
    print(a,end='',file=s)
    
print('''Append completed!
Content of "data.txt":''')
print(a)