#06NormalDistribution-p02CDF.py

"""
+---------------------+
| Normal Distribution |
+---------------------+
Cumulative Density function of Normal Distribution is given by :
    cdf(x | m,sd) = 0.5*(1+erf((x-m)/(sd*sqrt(2))))
Here erf = error function
"math" module in python contains 'erf' function

Using matplotlib to plot this :
"""
import matplotlib.pyplot as pyplot
import math

def normal_cdf(x:float, mean:float=0, std_dev:float=1) -> float :
    erf_val = (x-mean)/(std_dev*math.sqrt(2))
    result = 0.5 + 0.5*math.erf(erf_val)
    return result

xaxis = [i/10.0 for i in range(-70,70)]
#mean=0, standard deviation = 1
yaxis1 = [normal_cdf(i) for i in xaxis]
#mean=0, standard deviation = 2
yaxis2 = [normal_cdf(i,std_dev=2) for i in xaxis]
#mean=0, standard deviation = 0.5
yaxis3 = [normal_cdf(i,std_dev=0.5) for i in xaxis]
#mean=-1, standard deviation = 1
yaxis4 = [normal_cdf(i,mean=-1) for i in xaxis]
#mean=1, standard deviation = 1
yaxis5 = [normal_cdf(i,mean=1) for i in xaxis]

#plots
#mean=0, standard deviation = 1
pyplot.plot(xaxis, yaxis1, color='black', label='m=0,sd=1')
#mean=0, standard deviation = 2
pyplot.plot(xaxis, yaxis2, color='red', linestyle='-.', label='m=0,sd=2')
#mean=0, standard deviation = 0.5
pyplot.plot(xaxis, yaxis3, color='green', linestyle='-.', label='m=0,sd=0.5')
#mean=-1, standard deviation = 1
pyplot.plot(xaxis, yaxis4, color='blue', linestyle='-.', label='m=-1,sd=1')
#mean=1, standard deviation = 1
pyplot.plot(xaxis, yaxis5, color='yellow', linestyle='-.', label='m=1,sd=1')

pyplot.legend()
pyplot.title("Normal Distribution CDF with varying parameters")
pyplot.show()
