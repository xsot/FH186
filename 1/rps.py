for n in open(0).read().split('\n'):
    s=n.split()
    print(s[1]) if s[0]==2*s[1] or s[0]>s[1] else print(s[0])