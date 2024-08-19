n=int(input())
total=0
max_list=[]
min_list=[]
for i in range(n):
  x=int(input())
  if x<=0:
    min_list.append(x)
  elif x==1:
    total+=1
  else:
    max_list.append(x)
min_list.sort()
max_list.sort(reverse=True)

for i in range(0,len(min_list),+2):
  if i+1<len(min_list):
    total+=(min_list[i]*min_list[i+1])
  else:
    total+=min_list[i]
for i in range(0,len(max_list),+2):
  if i+1 < len(max_list):
    total+=(max_list[i]*max_list[i+1])
  else:
    total+=max_list[i]

print(total)