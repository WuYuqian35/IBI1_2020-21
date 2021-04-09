sizes=[29862124,11285561,11205972,4360823,4234924]
#input the statistics of five countries.
a=0
for i in range(len(sizes)):
    a=a+sizes[i]
#calculate the total number

frequency_dictionary={'USA':sizes[0]/a,'India':sizes[1]/a,'Brazil':sizes[2]/a,'Russia':sizes[3]/a,'UK':sizes[4]/a}
#input the information
print(frequency_dictionary)
#output the frequency_dictionary



import matplotlib.pyplot as plt
#use the Python package for 2D graohics.
labels='USA','India','Brazil','Russia','UK'
#labels five countries.

explode =(0,0,0,0,0)
#make the pie chart a complete one but not separated.
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.3f%%',shadow=True,startangle=90)
plt.title('Coronavirus rates')
#define the labels and other things of the chart. Autopct means the form of statistics.
plt.axis('equal')
#ensure that the chart is a circle.
plt.show()
#display the chart

