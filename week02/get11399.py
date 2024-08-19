n=int(input())
p=[]
p=list(map(int,input().split()))
p.sort()
for i in range(n-1,0,-1):
  for j in range(0,i):
    p[i]+=p[j]
total=0
for i in range(n):
  total+=p[i]
print(total)