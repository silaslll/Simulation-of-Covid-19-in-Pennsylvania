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



#input the cumulative case from 200 days to 360 days as y_data1
x_data= range(370)
y_data= graph.x1
x_data1= range(0,130)
y_data1= graph.x1[230:360]


#initialize the parameters: r is the growth rate, k is the carrying capacity
#popt is the optimization value for P0 , mse is the mean squared error
r = 0
k = 0
popt = 0
mse = float("inf")


#create a range of value for k and r to calculate the least square error
k_range = np.arange(900000, 1200000, 10000)
r_range = np.arange(0, 1, 0.01)


#use curve_fit and least square error to find best fitted parameter_K and parameter_r
'''
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


print(parameter_K ,parameter_r , popt)

'''

# the values are found by training data from 200 days to 360 days
parameter_K = 1070000
parameter_r = 0.03


#predic for 10 days
para_time = np.linspace(0, 140, 140)
time = np.linspace(230, 370,140)
xxx =  logistic_f(para_time, 147491.79516422)


#calculate the error
error_logi = np.abs(  y_data[360:370] - xxx[130:140])


#calculate the percentage of error
error_per = error_logi / y_data[360:370]



t2 = np.linspace(0, 10,10)
plt.plot(t2 , error_per )
plt.title("Error in the logistic model")
plt.xlabel('t(day)')
plt.ylabel('case')
plt.show()

