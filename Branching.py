import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error
import graph


# input cumulative data as Cumulative, existing cases as Existing
Cumulative = graph.x1
SIDR = graph.data
Existing = SIDR[1]


#create a list for the mean data and time range
mean = []
time = range(42 , len(Cumulative)-42)


#solve for the offspring mean using 42-day interval
for i in time:
    offspring = (Cumulative[i+42]-Cumulative[i] ) / Existing[i]
    mean.append(offspring)



#solve for the average value of offspring mean
averaglist = []
average = sum(mean)/len(mean)
averaglist2 = []
average2 = sum(mean[:226])/(len(mean)-60)




print(average)
print(average2)




for i in range(len(time)):
    averaglist.append(average)


# average value before vaccination
for i in range(len(time)):
    averaglist2.append(average2)



#plot the mean value and average values
plt.figure ()
p0, = plt.plot(time, mean)
p1, = plt.plot(time , averaglist )
p2, = plt.plot(time , averaglist2 )
plt.legend([p0,p1,p2], ["offspring","average","average before vaccination"])
plt.title("Branching process")
plt.xlabel('t(day)')
plt.ylabel('offspring mean')
plt.show()
