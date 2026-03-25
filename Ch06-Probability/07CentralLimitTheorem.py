#07CentralLimitTheorem.py

"""
+-----------------------+
| Central Limit Theorem |
+-----------------------+

Central limit theorem states that a random variable defined as the average of a large number of independent and identically distributed random variables is itself approximately normally distributed.

If x1,x2,...xn are 'n' independent and identically distributed random variables with mean 'm' and standard deviation 'sd' and 'n' is large, then :
    f1 = (x1+x2+...+xn)/n
This function f1 is normally distributed on mean 'm' and standard deviation 'sd/sqrt(n)'. Equivalently,
    f2 = ((x1+x2+...+xn)-(m*n))/(sd*sqrt(n))
is normally distributed on mean m=0 and standard deviation sd=1

This can be demonstrated using binomial random variables.
Consider a Binomial(n,p) random variable. Binomial random variable is the sum of 'n' independent Bernoulli(p) variables each of which equals 1 with probability p and 0 with probability 1-p
"""
import random

def bernoulli_trial(p:float) -> float:
    """
    Returns a bernoulli trial
    """
    if random.random() < p :
        return 1
    else :
        return 0

def binomial(n:int, p:float) -> float :
    """
    Returns sum of n bernoulli trials
    """
    return sum(bernoulli_trial(p) for _ in range(n))

import math

def normal_cdf(x:float, mean:float=0, std_dev:float=1) -> float :
    """
    Returns the Normal Cumulative Distribution Function
    """
    erf_val = (x-mean)/(std_dev*math.sqrt(2))
    result = 0.5 + 0.5*math.erf(erf_val)
    return result

import matplotlib.pyplot as pyplot
from collections import Counter

num_points = 10000
n = 100
p = 0.75

#Binomial cumulative distribution using binomial() function
data = [binomial(n,p) for _ in range(num_points)]
#print(data)
histogram = Counter(data)
pyplot.bar(histogram.keys(), [v/num_points for v in histogram.values()])
#divide by num_points in y axis for result to be in range 0-1

"""
For a bernoulli(p), mean is 'p' and standard deviation is 'sqrt(p*(1-p))'.
According to Central limit theorem, for a binomial(n,p) the mean should be n*p and standard deviation should be sqrt(n*p*(1-p))
"""

#CDF for data according to central limit theorem
mean = n*p
std_dev = math.sqrt(n*p*(1-p))
h=0.5 # Why 0.5?

xaxis = range(min(data),max(data)+1)
yaxis = [normal_cdf(x+h,mean=mean, std_dev=std_dev)-normal_cdf(x-h,mean=mean, std_dev=std_dev) for x in xaxis]
pyplot.plot(xaxis, yaxis, color='black')

#display plot
pyplot.show()
