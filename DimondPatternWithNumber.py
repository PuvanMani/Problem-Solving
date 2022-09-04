n=int(input("Enter the Number :"))
for i in range(n+1):
    for j in range(n-i):
        print(" ",end=' ')
    for x in range(1,i+1):
        print(i+1-x,end=' ')
    for j in range(i+1):
        print(j,end=' ')
    
    print()
for i in range(n+1):
    for m in range(1,i+1):
        print(" ",end=' ')
    for j in range(n-i):
        print(n-i-j,end=' ')
    for x in range(n+1-i):
        print(x,end=' ')
    print()
