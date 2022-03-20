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



for i in time:
    #subtract the data 42 days ago from the current data
    #and divided by the existing data 42 days ago
    #to calculate the offspring using 42-day intervals
    offspring = (Cumulative[i+42]-Cumulative[i] ) / Existing[i]
    mean.append(offspring)




#calculating the prediction value for day 1
prediction = []
offspring_predic1 = mean[-11]
cumulative_predic1 = offspring_predic1*Existing[-52] + Cumulative[-52]
prediction.append(cumulative_predic1)


# calculating the prediction value from day 2 to day 10
for i in range(0,9):
    #updating the offsrping using the prediction from the last day
    offspring_predic = (prediction[i] - Cumulative[-52+i] ) / Existing[-52+i]
    #using the predicted offspring to do the prediction for cumulative case
    cumulative_predic = offspring_predic * Existing[-51+i] + Cumulative[-51+i]
    prediction.append(cumulative_predic)



#compute the error
cumulative_data = Cumulative[-10:]
error_per_list = []
error_list = np.abs(np.array(cumulative_data )- np.array(prediction))


#compute the percent error
error_per = error_list/np.array(Cumulative[-10:])


#plot the error in the Branching process
time = np.linspace(0,10,10)
plt.plot(time, error_list)
plt.title("Error in the Branching process")
plt.xlabel('t(day)')
plt.ylabel('case')
plt.show()





