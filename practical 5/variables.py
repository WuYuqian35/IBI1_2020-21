a=251201
b=190784
c=100321
d=abs(a-c)
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
  
