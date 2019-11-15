while 1:
  a,b=map(int,input().split());print(str(('%f' % (a/10**b))).rstrip('0').rstrip('.'))