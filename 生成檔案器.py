for i in range(7,10):
    for j in range(1, 11):
        with open(file = f'{i}{j:02d}.py', mode = 'wt') as file:
            print('hello, world')