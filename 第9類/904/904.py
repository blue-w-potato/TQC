n,h,w = [], [], []
with open( 'read.txt', 'r' ) as s:
    a = s.read().replace('\n', '\n\n')
    print(a)
    for i in a.split('\n\n'):
        if len(i):
            d = i.split()
            n.append( d.pop(0) )
            h.append( int(d.pop(0)) )
            w.append( int(d.pop(0)) )
            
ah = f'{sum(h) / len(h):.2f}'
print('Average height:', ah)
aw = f'{sum(w) / len(w):.2f}'
print('Average weight:', aw)

m = h.index(max(h))
print(f'The tallest is {n[m]} with {h[m]:.2f}cm')

m = w.index(max(w))
print(f'The heaviest is {n[m]} with {w[m]:.2f}kg')
