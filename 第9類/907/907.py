w = input()

with open(w,'r') as s:
    e = s.read()
a,b,c = 0,0,0

c = len(e.replace(' ','').replace('\n',''))
a = len([i for i in e.split('\n') if i])
b = sum([len(i.split()) for i in e.split('\n')])

print(a,'line(s)')
print(b,'word(s)')
print(c,'character(s)')