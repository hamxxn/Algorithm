n=input()
num=list(n)
count=0
for i in range(len(num)):
  if num[i]!='X':
    count=0
  else:
    count+=1
    if count%2==0:
      if count%4==0:
        for j in range(i,i-count,-1):
          num[j]='A'
          count=0
      else:
        for j in range(i,i-count,-1):
          num[j]='B'
  
if 'X' in num:
  print(-1)
else:
  print("".join(num))