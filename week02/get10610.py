n=input()

if '0' in n:
  total=0
  for i in range(len(n)):
    total+=int(n[i])
  if total%3!=0:
    print(-1)
  else:
    n=sorted(n,reverse=True)
    print(''.join(n))
else:
  print(-1)
  