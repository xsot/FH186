d={}
while 1:
    n=input()
    if '?' in n:
        print(n.replace('?',d[n[abs(n.index('?')-2)]]))
    else:
        n=sorted(n.split('='))
        d[n[1]]=n[0]
