a = '\n'.join([ input() for i in range(5) ])
with open( 'write.txt', 'wt' ) as s:
    print(a, end='', file=s )