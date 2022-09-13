n=input("enter Some text Here :") 
for i in range(0,len(n),2):
    if i==len(n)-3:  
        print(n[i]*int((n[i+1]+n[i+2])))
        break
    else:
        print(n[i]*int(n[i+1]),end='')
