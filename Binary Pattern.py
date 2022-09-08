n=int(input("Enter the number :"))
for i in range(1,n+1):
    for x in range((n+1)-i-1):
        print(" ",end='')
    for j in range(i):
        print("10",end='')
    print()
