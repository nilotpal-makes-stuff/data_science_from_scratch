#06NormalDistribution-p01PDF.py

"""
+---------------------+
| Normal Distribution |
+---------------------+
Normal distribution is the classic bell curve-shaped distribution which is determined by two parameters :
    * mean(m) - Mean determines the center of the curve
    * standard deviation (sd) - Standard deviation determines the width of the curve.

Probability Density function of Normal Distribution is given by :
    f(x | m,sd) = (e^(-((x-m)^2)/2(sd)^2) )/ (sqrt(2*pi) * sd)

Using matplotlib to plot this :
"""
import matplotlib.pyplot as pyplot
import math

def normal_pdf(x:float, mean:float=0, std_dev:float=1) -> float :
    exp_pow = -((x-mean)**2)/(2*(std_dev**2))
    divisor = math.sqrt(2*math.pi) * std_dev
    result = math.exp(exp_pow)/divisor
    return result

xaxis = [i/10.0 for i in range(-70,70)]
#mean=0, standard deviation = 1
yaxis1 = [normal_pdf(i) for i in xaxis]
#mean=0, standard deviation = 2
yaxis2 = [normal_pdf(i,std_dev=2) for i in xaxis]
#mean=0, standard deviation = 0.5
yaxis3 = [normal_pdf(i,std_dev=0.5) for i in xaxis]
#mean=-1, standard deviation = 1
yaxis4 = [normal_pdf(i,mean=-1) for i in xaxis]
#mean=1, standard deviation = 1
yaxis5 = [normal_pdf(i,mean=1) for i in xaxis]

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
pyplot.title("Normal Distribution PDF with varying parameters")
pyplot.show()
