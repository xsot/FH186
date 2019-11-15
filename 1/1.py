while 1: n=input().split();n.sort(key=len);print(n[1] if len(n[1])-len(n[0])<4 else n[0])
