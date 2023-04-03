dat=[]
dat_rev=[]
x=input("enter the coordinates as a1,b1;a2,b2;.....an,bn")
import re
x1=re.split(";|'|,",x)
for k in x1:
    dat.append(float(k))
print(dat)
i=0
while i<len(dat):
    temp=[]
    temp.append(dat[i])
    temp.append(dat[i+1])
    dat_rev.append(temp)
    i=i+2
print(temp)    
print(dat_rev)
dat_rev=sort(datrev)

for i in range(len(dat_rev)):
    for j in range(i+1,len(dat_rev)):
        
      if dat_rev[i][0]>dat_rev[j][0]:
            temp=dat_rev[i]
            dat_rev[i]=dat_rev[j]
            dat_rev[j]=temp

    
s=0
for i in range(len(dat_rev)):
    s = s + (0.5*(dat_rev[0][1]+dat_rev[1][1])*((dat_rev[1][0]-dat_rev[0][0])))

print(s)
    


