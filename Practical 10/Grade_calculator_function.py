class Student(object):
    def __init__(self,n,co,po,ex):
        self.name=n
        self.code=co *0.4                         #students' code point proportion
        self.poster=po *0.3                      #poster proportion
        self.exam=ex *0.3                        #final exam proportion
    def speak(self):
        print(self.name,(self.code+self.poster+self.exam))      #the final grade is to add all the grades together
        return(self.name,(self.code+self.poster+self.exam))
print('Example: Wu Yuqian,70,80,90')
exm=Student('Wu Yuqian',70,80,90)                      #Example
print('The final grade is ')
exm.speak()
print("please input a student's name and his or her grades")
exm=Student(input(),float(input()),float(input()),float(input()))       #input the name and the grades and transfer the string into float
print('The final grade is ')
exm.speak()
