a = '@'.join([ input() for i in range(5) ])
for i in ('A1','J11','Q12','K13'):
    a = a.replace(i[0],i[1:])
print(sum(map(int,a.split('@'))))