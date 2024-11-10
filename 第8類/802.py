a = [ [j,ord(j)] for j in input() ]
for i,j in a:print(f'ASCII code for \'{i}\' is {j}')
print(sum([i[1] for i in a]))