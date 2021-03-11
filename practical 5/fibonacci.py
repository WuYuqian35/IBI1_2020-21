a=1
b=1
c=0
print(a,',',b)
#print the first two numbers

for i in range(1,12):
	c=a+b              #calculate the third number
	a=b                #every number moves forward
	b=c
	print(c,' ')       #print every answer we have calculated
