a = [int(input()) for i in range(10)]
a.remove(max(a))
a.remove(min(a))
print(sum(a))
print(f'{sum(a)/8:.2f}')