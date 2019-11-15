while 1:from decimal import *;d=Decimal;a,b=input().split();print("{:.99f}".format(d(a)/d(10**int(b))).rstrip('0').rstrip('.'))
