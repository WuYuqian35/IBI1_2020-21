a=1
b=1
c=0
print(a,',',b)
for i in range(1,12):
	c=a+b
	a=b
	b=c
	print(c,' ')
