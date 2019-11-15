while 1:
    n=input().split()
    n=int(n[0])/(10**int(n[1]))
    print(int(n) if n==int(n) else n)
