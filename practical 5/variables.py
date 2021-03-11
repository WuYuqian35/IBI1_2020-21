a=251201                                 #my birthday
b=190784                                 #Young's birthday
c=100321                                #today's date
d=abs(a-c)                              #the absolute difference
e=abs(b-c)
if d>e:
  print('d is greater')
else:
  print('c is greater')

  
x=False
y=True
z=(x and not y) or (y and not x)
print(z)

w=x!=y
if w==z:
  print(w==z)
  
