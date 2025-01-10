n,h,w = [],[],[]
with open('read.txt','r') as s:
    a = s.read().replace('\n','\n\n')
    print(a)
    for i in a.split('\n\n'):
        if i:
            e = i.split()
            n.append(e[0])
            h.append(int(e[1]))
            w.append(int(e[2]))
            
print(f'Average height: {sum(h)/len(h):.2f}')
print(f'Average weight: {sum(w)/len(w):.2f}')

m = h.index(max(h))
print(f'The tallest is {n[m]} with {h[m]:.2f}cm')
m = w.index(max(w))
print(f'The heaviest is {n[m]} with {w[m]:.2f}kg')