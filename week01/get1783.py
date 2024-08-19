def up1(up,down):
  global n_count, m_count,total 
  global up2r,up1r,down1r,down2r
  if m-m_count>=2 and n-n_count>=1:
    if up>0:
      up1r+=1
    else:
      down1r+=1
    n_count+=up
    m_count+=down
    total+=1 
    
def up2(up,down):
  global n_count, m_count,total
  global up2r,up1r,down1r,down2r
  if m-m_count>=1 and n-n_count>=2:
    if up>0:
      up2r+=1
    else:
      down2r+=1
    n_count+=up
    m_count+=down
    total+=1

n,m=map(int,input().split())
n_count, m_count,total =1,1,1
up2r,up1r,down1r,down2r=0,0,0,0
up2(2,1)
if n>=5 and m>=3:
  up2(2,1)
up2(-2,1)
up1(1,2)
up1(-1,2)
print(up1r,up2r,down2r,down1r)
if up2r!=0 and up1r!=0 and down2r!=0 and down1r!=0:
  if n<=3: 
    while True:
      if m-m_count>=2 and n-n_count>=1:
        up1(1,2)
      else: break
      if m-m_count>=2 and n-n_count>=1:
        up2(-1,2)
      else: break
  else:
    while True:
      if m-m_count>=1 and n-n_count>=2:
        up2(2,1)
      else: break
      if m-m_count>=1 and n-n_count>=2:
        up2(-2,1)
      else: break
print(total)
    
    
  
    
  