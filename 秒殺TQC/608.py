a = [int(input()) for i in range(9)] # 3*3
# 0 1 2
# 3 4 5
# 6 7 8
# r = n // 3
# c = n % 3

m = max(a); s = a.index(m)
print(f'Index of the largest number {m} is: ({s//3}, {s%3})')

# 複製上面的再改
m = min(a); s = a.index(m)
print(f'Index of the smallest number {m} is: ({s//3}, {s%3})')
