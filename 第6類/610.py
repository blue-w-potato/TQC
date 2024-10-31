a = []
for w in range(4):
    print(f'Week {w+1}:')
    for d in range(3):
        a.append(eval(input(f'Day {d+1}:')))
print(f'Average: {sum(a)/12:.2f}')
print(f'Highest: {max(a)}')
print(f'Lowest: {min(a)}')