for _ in range(int(input())):
    a = ''.join(input().upper().split())
    for i in range(65, 65+26):
        if chr(i) in a:
            continue
        print(False)
        break
    else:
        print(True)