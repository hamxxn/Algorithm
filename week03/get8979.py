N,k=map(int,input().split())
gm=[]
num=[]
for i in range(N):
  a,b,c,d=map(int,input().split())
  gm.append([a,b,c,d])
  num.append((i+1))
gm.sort(key=lambda x:(-x[1],-x[2],-x[3]))
idx=0
for i in range(N):
  if gm[i][0]==k:
    idx=i
  if i!=0:
    if gm[i][1]==gm[i-1][1] and gm[i][2]==gm[i-1][2] and gm[i][3]==gm[i-1][3]:
      num[i]=num[i-1]
print(num[idx])