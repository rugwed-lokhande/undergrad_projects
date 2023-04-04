import re
import numpy as np

dicto={"8":np.sqrt(15.99491),"1":np.sqrt(1.00783),"6":np.sqrt(12)}
f1=open("water_hpmodes",'r')
f=f1.readlines()
dat=[]
for k in f:
    dat.append(k.split())
dat1=[]
#flag=0
for k in dat:
    if k!=[]:
        dat1.append(k)

i=0
flag=0
dat2=[]
dat3=[]
t1=[]
t2=[]
rm=[]

while i<len(dat1):
    if dat1[i][0]=='Reduced':
    
        for k in dat1[i][3:len(dat1[i])]:
            rm.append(k)
    i=i+1

i=0
while i<len(dat1):

	if flag==1:
        
        atom=dat1[i][2]
        wt=dicto[atom]
        
        j=0
        #print(atom,wt)
        for k in dat1[i][3:len(dat1[i])]:
            
            t1[j].append(float(k)*wt)
            t2[j].append(float(k))
            j=j+1
           
        j=0
        for k in dat1[i+1][3:len(dat1[i+1])]:
            t1[j].append(float(k)*wt)
            t2[j].append(float(k))
            
            j=j+1
        j=0
        for k in dat1[i+2][3:len(dat1[i+2])]:
            t1[j].append(float(k)*wt)
            t2[j].append(float(k))
            j=j+1
            
        if i+3<=len(dat1):
            if i+4<len(dat1):
                if dat1[i+4][0] == 'A':
                    dat2=dat2+t1
                    dat3=dat3+t2
                    flag=0
                    t1=[]
                    t2=[]
            if i+3==len(dat1):
                    dat2=dat2+t1
                    dat3=dat3+t2
                    flag=0
                    t1=[]
                    t2=[]
                
            i=i+3




        
    
    if i<len(dat):    
        if dat1[i][0]=='Coord':
            t1=[] 
            t2=[]
            flag=1
            for k in dat1[i+1][3:len(dat1[i+1])]:
                t1.append(list([]))
                t2.append(list([]))
   

            i=i+1

    if flag==0:
        i=i+1

dat3_=[]           
for idx in range(len(dat3)):
    dat3_.append(np.divide(np.array(dat3[idx]),np.sqrt(float(rm[idx]))))

dat3=dat3_

res=[]
for k in dat2:
    t=[]
    for l in dat2:
        t.append(np.round(np.dot(np.array(k),np.array(l)),3))
    res.append(t)
res_=[]
for k in dat3:
    t=[]
    for l in dat3:
        t.append(np.round(np.dot(np.array(k),np.array(l)),3))
    res_.append(t)


for i in range(len(dat2)):
    res[i][i]=float(res[i][i])/float(rm[i])


f=open("water_input.txt", 'r')
x=f.readlines()
dat1_=[]
for k1 in x:
    dat1_.append(k1.split())
dat2_=[]
for k in dat1_:
    if k!=[]:
        for l in k[1:len(k)]:
            dat2_.append(float(l))


idx=int(input("enter the mode :"))
print(idx)
ct=float(input("enter the constant :"))
 
res_=np.add(dat2_,np.multiply(dat3[idx-1],ct))

print(res_)

file=open("output_res.txt",'w')
idx=0
while idx < len(res_):
    file.write(str(res_[idx]) + str("\t\t") + str(res_[idx+1]) + str("\t\t") + str(res_[idx+2]) +str("\n"))
    idx=idx+3
file.close()
    