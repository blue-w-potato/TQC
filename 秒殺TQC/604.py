a = [ int(input()) for i in range(10) ] # 10 個整數
n = [0,0] # 用來存出現次數最多的那個數 [ 那個數, 出現次數 ]
for i in set(a): # 去重複
    s = a.count(i) # 出現次數
    if s > n[1]: # 如果 出現次數 比目前最多的還多
        n = [i, s] # 更新紀錄
for i in n:print(i) # 分兩行輸出 n