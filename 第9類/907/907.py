with open('read.txt', 'r') as s:
    a = s.read()[:-1]
n = [0,0,0]
n[2] = len(a.replace('\n','').replace(' ',''))
a = a.split('\n')
n[0] = len(a)
n[1] = sum([ len(i.split()) for i in a ])
print(n[0],'line(s)')
print(n[1],'word(s)')
print(n[2],'character(s)')