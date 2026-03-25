#06NormalDistribution-p03InvertedCDF.py

"""
+---------------------+
| Normal Distribution |
+---------------------+
Cumulative Density function of Normal Distribution is sometimes inverted to find the value corresponding to a specific probability. This is called Inverse Cumulative Density Function(ICDF) or Quantile function.
    cdf(x | m,sd) = 0.5*(1+erf((x-m)/(sd*sqrt(2))))
Here erf = error function
"math" module in python contains 'erf' function
    icdf(x|m,sd) = m + sqrt(2)*sd*inverse_erf(2x-1)

Using matplotlib to plot this :
"""
import matplotlib.pyplot as pyplot
import math
import scipy.special

def normal_cdf(x:float, mean:float=0, std_dev:float=1) -> float :
    erf_val = (x-mean)/(std_dev*math.sqrt(2))
    result = 0.5 + 0.5*math.erf(erf_val)
    return result

#ICDF using formula
def inv_cdf(p:float, mean:float=0, std_dev:float=1) -> float :
    inverse_erf = scipy.special.erfinv(2*p-1)
    result = mean + math.sqrt(2)*std_dev*inverse_erf
    return result

#ICDF using binary search
def inv_cdf_binsrc(p:float, mean:float=0, std_dev:float=1, tolerance:float=0.00001) -> float :
    if mean!=0 or std_dev!=1 :
        return mean + std_dev*inv_cdf_binsrc(p, tolerance=tolerance)
    low=-10
    high=10
    while high-low > tolerance :
        mid_z=(low+high)/2
        mid_p=normal_cdf(mid_z)
        if mid_p<p :
            low = mid_z
        else :
            high = mid_z
    return mid_z


xaxis = [i/10.0 for i in range(-70,70)]
#Using inv_cdf() function
#mean=0, standard deviation = 1
yaxis1 = [inv_cdf(i) for i in xaxis]
#mean=0, standard deviation = 2
yaxis2 = [inv_cdf(i,std_dev=2) for i in xaxis]
#mean=0, standard deviation = 0.5
yaxis3 = [inv_cdf(i,std_dev=0.5) for i in xaxis]
#mean=-1, standard deviation = 1
yaxis4 = [inv_cdf(i,mean=-1) for i in xaxis]
#mean=1, standard deviation = 1
yaxis5 = [inv_cdf(i,mean=1) for i in xaxis]

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
pyplot.title("Normal Distribution ICDF (using inv_cdf())")
pyplot.show()

"""
Using binary search to obtain ICDF :
"""
xaxis = [i/10.0 for i in range(-50,50)]
#Using inv_cdf() function
#mean=0, standard deviation = 1
yaxis1 = [inv_cdf_binsrc(i) for i in xaxis]
#mean=0, standard deviation = 2
yaxis2 = [inv_cdf_binsrc(i,std_dev=2) for i in xaxis]
#mean=0, standard deviation = 0.5
yaxis3 = [inv_cdf_binsrc(i,std_dev=0.5) for i in xaxis]
#mean=-1, standard deviation = 1
yaxis4 = [inv_cdf_binsrc(i,mean=-1) for i in xaxis]
#mean=1, standard deviation = 1
yaxis5 = [inv_cdf_binsrc(i,mean=1) for i in xaxis]

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

pyplot.xlim([0,1])
pyplot.legend()
pyplot.title("Normal Distribution ICDF (using inv_cdf_binsrc())")
pyplot.show()
