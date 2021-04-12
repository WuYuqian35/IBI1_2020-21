import re
a=''                      #use a to store the sequences
Bool=False              #to test if it is the unknown gene function
count=0               #count all the unknown_function gene to check
dic={}                   #to store the final answers
genes_files=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')   #open the target file

genes={
'TTT':'F', 'TCT':'S', 'TAT':'Y', 'TGT':'C',
'TTC':'F', 'TCC':'S', 'TAC':'Y', 'TGC':'C',
'TTA':'L', 'TCA':'S', 'TAA':'O', 'TGA':'X',
'TTG':'L', 'TCG':'S', 'TAG':'U', 'TGG':'W',
'CTT':'L', 'CCT':'P', 'CAT':'H', 'CGT':'R',
'CTC':'L', 'CCC':'P', 'CAC':'H', 'CGC':'R',
'CTA':'L', 'CCA':'P', 'CAA':'Q', 'CGA':'R',
'CTG':'L', 'CCG':'P', 'CAG':'Z', 'CGG':'R',
'ATT':'I', 'ACT':'T', 'AAT':'N', 'AGT':'S',
'ATC':'I', 'ACC':'T', 'AAC':'B', 'AGC':'S',
'ATA':'J', 'ACA':'T', 'AAA':'K', 'AGA':'R',
'ATG':'M', 'ACG':'T', 'AAG':'K', 'AGG':'R',
'GTT':'V', 'GCT':'A', 'GAT':'D', 'GGT':'G',
'GTC':'V', 'GCC':'A', 'GAC':'D', 'GGC':'G',
'GTA':'V', 'GCA':'A', 'GAA':'E', 'GGA':'G',
'GTG':'V', 'GCG':'A', 'GAG':'E', 'GGG':'G'}
ls1=''                    #to store the gene name
for l in genes_files:       #check every line in the file
    if (re.findall('\w+\n',l)) and Bool:           #add the sequence and its length to the dic if it is from a unknown_function gene
        a=(a+l).replace('\n','')                   #add the sequence and remove the space
        dic[l1]=[l1,int(len(a)),a]                 #store the required data
    elif (l.startswith('>')) and ('unknown function' in l):     #determine if the function of the gene is unknown
        Bool=True                                 #the flag becomes true if it is a unknown_function gene
        count=count+1                            #counter
        l1=str(re.findall(r'gene:\S+\s',l))         #store the name information of the gene to l1
        a=''                                       #clear the a to clear the previous data
    else:
        Bool=False                             #if the target gene is not found then the flag becomes false
        a=''                                    #clear the a to clear the previous data

unknown_function=open('unknown_function.fa','w')  #create a new file
for d in dic:
    unknown_function.write(str(dic[d]))           #read in all the data
    unknown_function.write('\n')                  #use space to make it more neat
genes_files.close()                           #close all files
unknown_function.close()
