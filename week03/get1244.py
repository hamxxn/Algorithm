def changeValue(a):
    if sw[a] == 1:
        sw[a]=0
    else:
        sw[a]=1

n=int(input())
sw = []
sw=list(map(int,input().split()))
N=int(input())
st=[]
for i in range(N):
  a,b=map(int,input().split())
  st.append([a,b])
for i in range(N):
  if st[i][0]==1:
    count=1
    while(count*st[i][1]<=n):
      changeValue(count*st[i][1]-1)
      count+=1
  else:
    changeValue(st[i][1]-1)
    idx=1
    while (st[i][1]-1-idx>=0) and (st[i][1]-1+idx<n):
      if sw[st[i][1]-1-idx]==sw[st[i][1]-1+idx]:
        changeValue(st[i][1]-1-idx)
        changeValue(st[i][1]-1+idx)
        idx+=1
      else:
        break
for i in range(n):
  print(sw[i],end=" ")
  if (i+1)%20==0:
    print()