n=input("Enter have non-Zero Number here :")
for i in n:
    i=int(i)
    if i>=ord('a') or i<=ord('z'):
        print(chr(i+64),end=' ')
print()
           #532426
n1=len(n)  #4
let=''
count=0
if n1%2==0:  
    for i in range(n1):  
        let+=n[i]  
        if count%2==0:
            count+=1   
            continue
        else:
            count+=1
        if count%2==0:
            if int(let)<=26:
                print(chr(int(let)+64),end='')
                let=''
            else:
                for a in let: 
                    print(chr(int(a)+64),end='')
                    let=''
else:
    for i in range(n1): 
        let+=n[i] 
        if count%2==0: 
            count+=1
            continue
        else:
            count+=1
        if count%2==0:
            if int(let)<=26: 
                print(chr(int(let)+64),end='') 
                let=''
                count+=1
            else:
                for a in let:
                    print(chr(int(a)+64),end='')
                let=''
                count+=1
        else:
            print(chr(int(let)+64),end='')
