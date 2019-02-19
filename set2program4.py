h=(raw_input())
p=0
for i in range(2,p//3):
    if(h%i==0):
        p=p+1
if(p<=0):
    print("yes")
else:
    print("no")
