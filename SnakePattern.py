inp=int(input("Enter the Number :"))
strt=inp
k=1
no=0
for x in range(1,inp+1):
    for i in range(inp-x):
        print(" ",end=' ')
    strt=1
    if x%2!=0:
        no+=inp+1
        for j in range(strt,inp+strt):
            print(k,end=' ')
            k+=1
    else:
        no+=inp
        for j in range(1,inp+1):
            print(no-j,end=' ')
            k+=1
        no-=1
    print()
