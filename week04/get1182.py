from itertools import combinations

global total
total=0
n,s=map(int,input().split())
num=list(map(int,input().split()))

def get_com(i):
  global total
  for com in combinations(num,i):
    if sum(com)==s:
      total+=1

for i in range(1,n+1):
  get_com(i)
print(total)