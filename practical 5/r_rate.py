n=84                                       #the initial number
r=1.1                                      #the increasing rate
for i in range(1,6):
  n=n*r+n                                    #the infected people in every round

print('r rate',r,',','infection:',n)
