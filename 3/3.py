s={}
while 1:
  a,b = input().split("=")
  if(a=='?'):
    print(s[b]+'='+b)
  elif(b=='?'):
    print(a+'='+s[a])
  else:
    s[b]=a
    s[a]=b
    
