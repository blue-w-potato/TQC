def compute(): # 題目說要建立函式
    r = int(input())
    c = int(input())
    
    for i in range(r):
        for j in range(c):
            print(f'{j-i:4}', end='') # 規律，仔細看範例看會發現
        print()

compute() # 在主程式中調用