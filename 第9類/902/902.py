with open('read.txt','rt') as s:
    print( sum( list(map(int, s.readline().split())) ) )