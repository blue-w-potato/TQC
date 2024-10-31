a = [int(input()) for i in range(10)]
s = list(set(a))
n = [0,0]
for i in s:
    if a.count(i) > n[1]:
        n = [i,a.count(i)]
for i in n:print(i)