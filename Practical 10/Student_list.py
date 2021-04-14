class Student(object):
    def __init__(self,n,s):
        self.name = n                   #define name
        self.subject = s               #define the undergraduate programme
    def speak(self):
        print(self.name,self.subject)
        return(self.name,self.subject)

print('Example:')
exm=Student('Wu Yuqian','BMS')         #exmaple
exm.speak()

bool=True
while bool==True:                #enable to input a list of students
    print('please input the name and the undergraduate programme:')
    output=Student(input(),input())   #input the name and subject
    print('continue?(y/n):')           #to decide whether to continue
    j=input()
    if j=='y'or j=='Y':                 #if the answer is yes then continue to input
        bool=True
    elif j=='n' or j=='N':           #else the loop will break
        bool=False

    else:
        bool=False
