import matplotlib.pyplot as plt
import numpy as np


#read the PA data file
f = open("pennsylvania.csv", "r")

h = f.readline().split(",")


s = []
for i in range(7):
    s.append([])


for l in f:

    # Create a list of the pandemic data
    d = l.split(",")

    s[0].append(d[0])
    s[1].append(d[1])

    for i in range(5):

        s[i + 2].append(int(d[i + 2]))

# x is the cumulative case

x = s[3][:370]
x1 = x[::-1]

# a is susceptible  b is infected  c is death  d is recovered

a = s[6][:370]
a1 = a[::-1]

b=s[5][:370]
b1=b[::-1]

c=s[2][:370]
c1=c[::-1]

d=s[4][:370]
d1=d[::-1]


# create a list of susceptible, infected, death, recovered data
data = np.array([a1,b1, c1 ,d1] )


f.close()