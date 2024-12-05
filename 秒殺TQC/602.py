# A = 1
# J = 11
# Q = 12
# K = 13

a = ' '.join([ input() for i in range(5) ]) # 把五張牌的點數用空格隔開
for i in ('A1', 'J11', 'Q12', 'K13'):
    a = a.replace(i[0], i[1:]) # i[0] 是字母 ， 字母後面全部的字是他的點數
print(sum(map(int, a.split()))) # a 用空格隔開所以這裡用空個切開，全部轉整數之後再加總