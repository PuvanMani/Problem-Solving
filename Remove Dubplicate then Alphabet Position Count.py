inp1=input("Enter the Word:").lower()
inp2=input("Enter the Word:").lower()
out=''
out2=''
outcount=0
for i in inp1:
    if i not in inp2:
        out+=i
    else:    
        outcount+=1
for i in inp2:
    if i not in inp1:
        out2+=i
final=0
count=0
output=''
output2=''
for i in out:
	for j in range(ord('a'), ord('z')+1):
		count+=1
		if i==chr(j):
			final+=count
			count=0
			break
output+=str(final)
final=0
count=0
for i in out2:
	for j in range(ord('a'), ord('z')+1):
		count+=1
		if i==chr(j):
			final+=count
			count=0
			break
output2+=str(final)
if outcount==0:
	print(output+output2)
else:
	print(str(outcount)+output+output2)
