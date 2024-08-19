t=int(input())
num=[]
for i in range(t):
  a,b=map(int,input().split())
  num.append([a,b])
for i in range(t):
  num2=[]
  for j in range(num[i][0],num[i][1]+1):
    num2.append(str(pow(2,j)))
  number=int(''.join(num2))
  count=num[i][1]
  get2=pow(2,count)
  while number%get2==0:
    count+=1
    get2*=2
  print(count-1)
  