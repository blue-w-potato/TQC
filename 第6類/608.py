a = [int(input()) for i in range(9)]
print(f'''Index of the largest number {max(a)} is: ({a.index(max(a))//3}, {a.index(max(a))%3})
Index of the smallest number {min(a)} is: ({a.index(min(a))//3}, {a.index(min(a))%3})''')