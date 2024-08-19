girl, boy, intern=map(int,input().split())
team=0
girlcount=girl//2
if girlcount<=boy:
  team+=girlcount
  boy-=girlcount
  girl-=girlcount*2
else:
  team+=boy
  girl-=boy*2
  boy=0
while True:
  if boy+girl>=intern:
    break
  else:
    team-=1
    girl+=2
    boy+=1
print(team)

n, m, k=map(int,input().split())
team=0
for i in range(k):
  if n//2>m:
    n-=1
  else:
    m-=1
print(min(n//2,m))