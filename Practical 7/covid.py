import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import all the necessary things


os.chdir("C:\\Users\\wyq\\desktop\\python")       #The code for importing the csv
covid_data=pd.read_csv("full_data.csv")          #create a new space for store the data


covid_data.iloc[0:11:2,:]            #correct code for showing all columns, and every second row between (and including 0 and 10)
                                    #starts from 0,ends at 11 (don't include 11), the interval is 2


my_rows=covid_data['location']=='Afghanistan'   #To see if the location is Afghanistan, the value 'my_rows' is a Boolean.
covid_data.loc[my_rows,'total_cases']         #To show the data we want


world_data=covid_data.loc[covid_data['location']=='World',['date','new_cases']]   #create a new space to store the data of the world
world_new_cases=world_data.iloc[:,1]            #store the new cases data
world_new_cases.median()                      #calculate the median
world_new_cases.mean()                        #calculate the mean


world_data.boxplot()                    #make the graph including only new_cases
plt.ylabel('new cases number')         #label the y axis
plt.show()                           #show the plot


world_data1=covid_data.loc[covid_data['location']=='World',['date','new_cases','new_deaths']]     #another one especially for new_deaths
world_data1.boxplot()                    #make the graph
plt.ylabel('Infected number')            #label the y axis
plt.show()                              #show the graph




#countries=covid_data['total_cases']<10
#countries=countries.tolist()
#date=covid_data['date']=='2020/3/31'
#all=date & countries
#all=all.tolist()
#print(covid_data.loc[countries,'location'])

countries_date_data=covid_data.loc[covid_data['total_cases']<10,['date','location']]       #To find out countries which has total cases less than 10
#countries_date_data=countries_date_data.tolist()
countries_date_data1=countries_date_data.loc[countries_date_data['date']=='2020-03-31','location']  #TO find the last day
print(countries_date_data1)
#countries=countries_date_data['total_cases']<10
#print(covid_data.loc[countries,'location'])
