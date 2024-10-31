t = []
for w in ('1st', '2nd', '3rd'):
    print(f'The {w} student:')
    t.append(sum([int(input()) for i in range(5)]))

for i in range(3):
    print(f'''Student {i+1}
#Sum {t[i]}
#Average {t[i]/5:.2f}''')