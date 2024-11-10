a = input().split('-')
if len(a) == 3:
    if len(a[0]) == 3 and len(a[1]) == 2 and len(a[2]) == 4:
        for i,j in enumerate((3,2,4)):
            try:
                for e in range(j):
                        int(a[i][e])
            except:
                print('Invalid SSN')
                break
        else:
            print('Valid SSN')
    else:
        print('Invalid SSN')
else:
    print('Invalid SSN')