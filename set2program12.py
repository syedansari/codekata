p=int(raw_input())
q=0
r=1
while p!=0:
    o=p%10
    q=q*10+o
    p=p/10
if q==r:
      print("yes")
      
else:
    
      print("no")
