d,q={},'?'
while 1:
 s=input();l,r=s.split('=')
 if l==q:l,r=(r,l)
 if r==q:print(s.replace(q,d[l]))
 elif r.isdigit():r,l=(l,r)
 d[r]=l