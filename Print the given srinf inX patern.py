
imp='geeksforgeeks'

for i in range(1,len(imp)+1):
    for j in range(1,len(imp)+1):
        if i==j or len(imp)+1-i==j: 
            print(imp[j-1],end=' ')
        else:
            print(' ',end=' ')
    print()
