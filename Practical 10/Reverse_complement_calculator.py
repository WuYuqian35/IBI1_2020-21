def reverse():
    str1=str
    output=''
    genes={'a':'T','A':'T','T':'A','t':'A','g':'C','G':'C','C':'G','c':'G'}            #The corresponding relationships between genes
    for i in range(0,len(str1)):
        output=output+genes[str1[i]]                                                   #find every corresponding gene
    output=output[::-1]                                                               #reverse the string
    print(output)
    return(output)


print('example:ACTGaacgact')    #exmaple
str='ACTGaacgact'
reverse()
print('please input a string:')   #input
str=input()
reverse()
