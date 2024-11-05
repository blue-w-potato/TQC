a = set()
while True:
    n = int(input())
    if n == -9999:break
    a.add(n)
print('Length:',len(a))
print('Max:',max(a))
print('Min:',min(a))
print('Sum:',sum(a))