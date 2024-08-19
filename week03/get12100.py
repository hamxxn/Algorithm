from itertools import product
from copy import deepcopy
def rigth(number):
  for i in range(n):
    idx=n-1
    value=0
    for j in range(n-1,-1,-1):
      if number[i][j]!=0:
        value=number[i][j]
        number[i][j]=0
        if number[i][idx]==0:
          number[i][idx]=value
        elif value==number[i][idx]:
          number[i][idx]*=2
          idx-=1
        else:
          idx-=1
          number[i][idx]=value
  return number
  
def left(number):
  for i in range(n):
    idx=0
    value=0
    for j in range(0,n):
      if number[i][j]!=0:
        value=number[i][j]
        number[i][j]=0
        if number[i][idx]==0:
          number[i][idx]=value
        elif value==number[i][idx]:
          number[i][idx]*=2
          idx+=1
        else:
          idx+=1
          number[i][idx]=value
  return number

def down(number):
  for i in range(n):
    idx=0
    value=0
    for j in range(0,n):
      if number[j][i]!=0:
        value=number[j][i]
        number[j][i]=0
        if number[idx][i]==0:
          number[idx][i]=value
        elif value==number[idx][i]:
          number[idx][i]*=2
          idx+=1
        else:
          idx+=1
          number[idx][i]=value
  return number
          
def up(number):
  for i in range(n):
    idx=n-1
    value=0
    for j in range(n-1,-1,-1):
      if number[j][i]!=0:
        value=number[j][i]
        number[j][i]=0
        if number[idx][i]==0:
          number[idx][i]=value
        elif value==number[idx][i]:
          number[idx][i]*=2
          idx-=1
        else:
          idx-=1
          number[idx][i]=value
  return number
def findMax(number):
  Max=0
  for i in range(len(number)):
    for j in range(len(number[0])):
      if Max< number[i][j]:
        Max=number[i][j]
  return Max
n=int(input())
number=[]
di=["up","down","rigth","left"]
for i in range(n):
  number.append(list(map(int,input().split())))
di=list(product(di,repeat=5))
Max=0

for i in range(len(di)):
  get=deepcopy(number)
  for j in range(5):
    if di[i][j]=="up":
      get=up(get)
    elif di[i][j]=="down":
      get=down(get)
    elif di[i][j]=="rigth":
      get=rigth(get)
    elif di[i][j]=="left":
      get=left(get)
  if Max< findMax(get):
    Max=findMax(get)
print(Max)