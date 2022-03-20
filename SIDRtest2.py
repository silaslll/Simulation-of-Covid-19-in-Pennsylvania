import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import curve_fit
import graph
import logistictest2
import Branchingtest2



ddd = graph.data

#input the initial data
initial= np.array([1006685 ,28163, 8500 , 146652])



# create SIRD differential equation
def deriv(X, t ,a,b,c):
	S, I, D, R = X
	ds = - S * I * a
	di = S * I * a - c * I - b * I
	dd = b * I
	dr = c * I
	return np.array([ds, di, dd, dr])



#create the function to solve the differential equation and output the I value
def fitfunc(t ,a,b,c,) :
	return odeint(deriv,initial,t,args=(a,b,c))[:,1]



#input the infected case as y_data
time =   np.linspace(0, 110,110)
xdata = np.array(time)
ydata = np.array(ddd[1], dtype=float)
t =  np.linspace(230, 340,110)


#find the best fitted curve with data from 230 days to 340 days
popt,pcov= curve_fit(fitfunc,xdata,ydata[230:340],p0=(0,0,0))

print(popt)


#predict for 30 days
xdata1 = np.linspace(0, 140,140)
t1 =  np.linspace(230, 370,140)
fitted = fitfunc(xdata1 ,*popt )



#calculate the error
error_S = np.abs(  ydata[340:370] - fitted[110:140])


#calculate the percent error
error_per = error_S / ydata[340:370]


#plot the error in SIRD model in 30 days
t2 = np.linspace(0, 30,30)
plt.plot(t2 , error_S )
plt.title("Error in the SIRD model")
plt.xlabel('t(day)')
plt.ylabel('case')
plt.show()



# input the error in other 2 models
error_log = logistictest2.error_per
error_bran = Branchingtest2.error_per



#plot the percent error in three models
t2 = np.linspace(0, 30,30)
p1,= plt.plot(t2 , error_per )
p2,= plt.plot(t2 , error_log )
p3,= plt.plot(t2 , error_bran  )
plt.legend([p1,p2,p3], ["percent error(SIRD)","percent error(logistic)","percent error(Branching process)"])
plt.title("percent error")
plt.xlabel('t(day)')
plt.ylabel('percentage')
plt.show()



