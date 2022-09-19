arr=[1,2,3,4,5,6,7,8,9]
count=0
temp=[]
temp2=[]
for i in arr:
    count+=1
    if count%2!=0:
        temp.append(i)
    else:
        temp2.append(i)

temp=sorted(temp)[::-1]
temp2=sorted(temp2)

finalarr=[]
count=0
for i in range(len(arr)):
    if i==0:
        finalarr.append(temp[i])
    elif i%2==0:
        finalarr.append(temp[i-count])
    else:
        finalarr.append(temp2[count])
        count+=1

print(finalarr)
        
        
        
