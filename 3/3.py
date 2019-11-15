c={}
while 1:
 x=input();a,b=sorted(x.split("="))
 if a=="?":print(x.replace("?",c[b]))
 else:c[b]=a
