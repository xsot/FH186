while 1:    
    a,b=input().split()
    if int(b) < len(a): print('{0:g}'.format(int(a)/10**int(b)))
    else: print('0.'+('0'*(len(a)-int(b))+a.rstrip('0')))