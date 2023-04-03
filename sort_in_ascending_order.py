#enter your file name in place of input
#input files contain numbers seperated by lines
f=open("input",'r')
data=f.read()
data=data.split("\n")
length=int(data[0])
data_rev=[]
for i in range(length):
    data_rev.append(float(data[i+1]))

Numlist=data_rev
Number=len(data_rev)
for i in range (Number) :
    for j in range(i+1, Number):
        if(Numlist[i] > Numlist[j]):
           temp = Numlist[i]
           Numlist[i] = Numlist[j]
           Numlist[j] = temp
print("Element after sorting list in ascending order is:", Numlist)

#enter output file name in place of output          
f=open("output.txt",'w')
for k in Numlist:
    f.write(str(k)+"\n")
f.close()
