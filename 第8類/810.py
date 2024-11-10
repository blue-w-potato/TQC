for _ in range(int(input())):
    a = list(map(eval,input().split()))
    print(f"{max(a)-min(a):.2f}")