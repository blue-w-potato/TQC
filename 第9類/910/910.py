with open('read.dat', 'r', encoding='utf-8') as s:
    a = s.read().split('\n')
print('\n\n'.join(a))
a = ''.join([i.split()[2] for i in a])
print('Number of males:', a.count('1'))
print('Number of females:', a.count('0'))