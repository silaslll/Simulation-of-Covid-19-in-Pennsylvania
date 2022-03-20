import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import curve_fit
import graph


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




time =   np.linspace(0, 140,140)



#input the infected case as y_data and create the time range from 230 days to 370 days
xdata = np.array(time)
ydata = np.array(ddd[1], dtype=float)
t =  np.linspace(230, 370,140)


#find the best fitted curve and value
popt,pcov= curve_fit(fitfunc,xdata,ydata[230:370],p0=(0,0,0))




#plot the image of fitted line and the data
xdata1 = np.linspace(0, 180,180)
t1 =  np.linspace(230, 410,180)
fitted = fitfunc(xdata1 ,*popt )
p0 = plt.plot(t , ydata[230:370])
p1 = plt.plot(t1 , fitted )
plt.title("Infected")
plt.xlabel('t(day)')
plt.ylabel('case')
plt.show()
