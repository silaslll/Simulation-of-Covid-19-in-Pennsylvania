import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error
import graph



# create logistic function
def logistic_f(t, P0):
    r = parameter_r
    K = parameter_K
    exp_value = np.exp(r * (t))
    return (K * exp_value * P0) / (K + (exp_value - 1) * P0)



#input the cumulative case from 200 days to 370 days as y_data1
x_data= range(370)
y_data= graph.x1

x_data1= range(0,170)
y_data1= graph.x1[200:370]



#initialize the parameters: r is the growth rate, k is the carrying capacity
#popt is the optimization value for P0 , mse is the mean squared error
r = 0
k = 0
popt = 0
mse = float("inf")


#create a range of value for k and r to calculate the least square error
k_range = np.arange(900000, 1200000, 10000)
r_range = np.arange(0, 1, 0.01)




#find the best fitted curve and values
for k_ in k_range:
    parameter_K = k_
    for r_ in r_range:
        parameter_r = r_
        popt_, pcov_ = curve_fit(logistic_f, x_data1, y_data1, maxfev=4000)
        mse_ = mean_squared_error(y_data1, logistic_f(x_data1, *popt_))
        if mse_ <= mse:
            mse = mse_
            popt = popt_
            r = r_
            k = k_

parameter_K = k
parameter_r = r
popt, pcov = curve_fit(logistic_f, x_data1, y_data1)


print(parameter_r , popt)



para_time = np.linspace(0, 200, 1000)
time = np.linspace(200, 400,1000)
xxx =  logistic_f(para_time, 69580.44125933)



#plot the image of fitted line and the data
plt.figure ()
p0, = plt.plot(range(370), y_data)
p1, = plt.plot(time , xxx )

plt.legend([p0,p1], ["data","prediction"])
plt.title("Covid 19 in PA")
plt.xlabel('t(day)')
plt.ylabel('cumulative case')
plt.show()
