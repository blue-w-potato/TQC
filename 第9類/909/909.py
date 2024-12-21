a = '\n'.join([input() for i in range(5)])

# 不用寫入
# with open('data.dat', 'wt') as s:
#     print(a,end='',file=s)
# print('The content of "data.dat":')

a += '\n'
print(a.replace('\n','\n\n'))