a = input()
print(a.upper())
print(*[i.capitalize() for i in a.split()])