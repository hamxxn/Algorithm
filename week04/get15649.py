n,m=map(int,input().split())
num=[]
def backtrack():
    if len(num)==m:
      for i in range(len(num)):
        print(num[i], end=" ")
      print()
      return
    for i in range(1,n+1):
        if not (i in num):
            num.append(i)
            backtrack()
            num.pop()
for i in range(1, n+1):
  num.append(i)
  backtrack()
  num.pop()