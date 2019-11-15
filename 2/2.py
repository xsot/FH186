while 1:
  a,b=map(int,input().split());print(str('{:.100f}'.format(a/10**b)).rstrip('0').rstrip('.'))