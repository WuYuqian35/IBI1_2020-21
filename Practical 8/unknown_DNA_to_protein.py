import re
a=''                      #use a to store the sequences
Bool=False              #to test if it is the unknown gene function
count=0               #count all the unknown_function gene to check
dic={}                   #to store the final answers
print('	input a	filename as	the	new	fasta file to be written to')
input=input()                        #let user to input a file name
A=open(input,'w')
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
ls1=''
p=''
for l in genes_files:
    if (re.findall('\w+\n',l)) and Bool:
        a=(a+l).replace('\n','')
        for i in range(0,len(a),3):                         #find the proteins
            p=p+genes[a[i:i+3]]
            dic[l1]=[l1,int(len(a)/3),p]
    elif (l.startswith('>')) and ('unknown function' in l):
        Bool=True
        count=count+1
        l1=str(re.findall(r'gene:\S+\s',l))
        a=''
    else:
        Bool=False
        a=''
        p=''
for d in dic:
    A.write(str(dic[d]))         #read in all the data
    A.write('\n')                  #use space to make it more neat
genes_files.close()                           #close all files
A.close()
