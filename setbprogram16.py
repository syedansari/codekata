f,g=raw_input().split()
f=int(f)
g=int(g)
for i in range(f+1,g):
    if i>1:
        for j in range (2,i):
         if(i%j==0): 
          break
        else:
         print(i),
