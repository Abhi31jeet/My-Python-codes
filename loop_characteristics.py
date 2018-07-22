l=[1,2,3]
while(l):
  c = len(l)
  if l[0]==3:
    l.append(4)
    l.append(5)
  print(l,c)
  l.pop(0)
