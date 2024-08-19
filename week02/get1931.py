n=int(input())
meeting=[]
for i in range(n):
  a,b=map(int,input().split())
  meeting.append([a,b])
meeting.sort(key=lambda x: (x[1],x[0]))
time=0
answer=0 
for meetings in meeting:
  if time<=meetings[0]:
    time=meetings[1]
    answer+=1
print(answer)
