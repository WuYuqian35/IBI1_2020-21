import numpy as np
gene_lengths=np.array([9410,394141,4442,105338,19149,76779,126550,36296,842,15981])
exon_counts=np.array([51,1142,42,216,25,650,32533,57,1,523])
#input the data
average=gene_lengths/exon_counts
#calculate the average
average_change=list(average)
average_change=sorted(average_change)
#change the variable form of the average from array to list
print(average_change)

import matplotlib.pyplot as plt
plt.boxplot(average_change,notch=False,showmeans=True,boxprops={'color':'green'})
#show the mean of the boxplot, change the color of the outline into green
plt.show()

#plt.violinplot(average_change)
#plt.show()
