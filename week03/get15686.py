from itertools import combinations
n,m=map(int,input().split())
get1=[]
get2=[]
nn=[]
for i in range(n):
  nn=list(map(int,input().split()))
  if 1 in nn or 2 in nn:
    for j in range(0,len(nn)):
      if nn[j]==1:
        get1.append([i,j])
      elif nn[j]==2:
        get2.append([i,j])
result=99999
for ch in combinations(get2,m):
  total=0
  for h in get1:
    house=99999
    for j in range(m):
     house=min(house,abs(h[0]-ch[j][0])+abs(h[1]-ch[j][1]))
    total+=house
  result=min(total,result)
print(result)