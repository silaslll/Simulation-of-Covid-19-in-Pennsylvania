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


#input the cumulative case from the first day to 370 days as y_data
x_data= range(370)
y_data= graph.x1



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
        popt_, pcov_ = curve_fit(logistic_f, x_data, y_data, maxfev=4000)
        mse_ = mean_squared_error(y_data, logistic_f(x_data, *popt_))
        if mse_ <= mse:
            mse = mse_
            popt = popt_
            r = r_
            k = k_

parameter_K = k
parameter_r = r
popt, pcov = curve_fit(logistic_f, x_data, y_data)


print(parameter_K ,parameter_r , popt)




time = np.linspace(0, 400,1000)
xxx =  logistic_f(time,2920.86447 )



#plot the image of fitted line and the data
plt.figure ()
p0, = plt.plot(range(370), y_data)
p1, = plt.plot(time , xxx )
plt.legend([p0,p1], ["data","prediction"])
plt.title("Covid 19 in PA")
plt.xlabel('t(day)')
plt.ylabel('cumulative case')
plt.show()













