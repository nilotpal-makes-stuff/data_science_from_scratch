#01Statistical_Hypothesis_Testing.py

"""
+--------------------------------+
| Statistical Hypothesis Testing |
+--------------------------------+

The science part of 'Data Science' frequently involves forming and testing hypotheses about data and the processes that generate it.

Data Scientist's task is to test whether a certain hypothesis is likely to be true. Hypothesis are assertions that can be translated into statistics about data.
Under various assumptions, those statistics can be thought of as observations of random variables from known distributions - this allows us to make statements about how likely the assumptions are to hold.

In classical setup, we have a 'Null hypothesis' H0 representing some default position and some alternate hypothesis H1 that we would like to compare it to. We use statistics to decide whether we can reject H0 as false or not.

+---------------------------+
| Example : Flipping a coin |
+---------------------------+
Consider a coin we want to test whether the coin is fair.
Assumption :
    * Null hypothesis H0 - Coin has some probability p=0.5 of landing heads -
    * Alternative hypothesis H1 - Coin has probability p!=0.5 for landing heads

Our test involves flipping a coin 'n' times and count the number of heads. Each coin flip is a Bernoulli trial and the experiment is a Binomial random variable. We can approximate using the normal distribution.
"""
from typing import Tuple
import math

def normal_approximation_to_binomial(n:int, p:float) -> Tuple[float, float] :
    """
    Return mean and standard deviation for Normal Distribution corresponding to Binomial
    """
    mean = p*n
    std_dev = math.sqrt(p*(1-p)*n)
    return (mean, std_dev)

"""
Since random variable follows normal distribution, we can use Normal Cumulative Distribution Function to get probability that realised value lies within or outside particular interval

Normal cdf and icdf functions
"""
def normal_cdf(x:float, mean:float=0, std_dev:float=1) -> float :
    """
    Return Normal Cumulative Distribution Function result
    """
    erf_val = (x-mean)/(std_dev*math.sqrt(2))
    result = 0.5 + 0.5*math.erf(erf_val)
    return result

import scipy.special
def normal_icdf(p:float, mean:float=0, std_dev:float=1) -> float :
    """
    Return Normal Inverse Cumulative Distribution Function result
    """
    inverse_erf = scipy.special.erfinv(2*p-1)
    result = mean + math.sqrt(2)*std_dev*inverse_erf
    return result

"""
Normal CDF is the probability the variable is below a threshold - normal_probability_below()
If variable is not below threshold it is above threshold - normal_probability_above()
It is between if it is less than 'hi' but greater than 'lo' - normal_probability_between()
It is outside if it is not in between - normal_probability_outside()
"""
#below
normal_probability_below = normal_cdf

#above
def normal_probability_above(lo:float, mean:float=0, std_dev:float=1) -> float :
    """
    Probability that an N(mean, std_dev) is greater than 'lo'
    """
    return 1-normal_cdf(lo, mean, std_dev)

#between
def normal_probability_between(lo:float, hi:float, mean:float=0, std_dev:float=1) -> float :
    """
    Probability that an N(mean, std_dev) is between 'lo' and 'hi'
    """
    return normal_cdf(hi, mean, std_dev) - normal_cdf(lo, mean, std_dev)

#outside
def normal_probability_outside(lo:float, hi:float, mean:float=0, std_dev:float=1) -> float :
    """
    The probability that an N(mean, std_dev) is outside
    """
    return 1-normal_probability_between(lo, hi, mean, std_dev)

"""
We can also do the reverse - find the nontail region or the symmetric inverval around the mean that accounts for a certain level of likelihood.
"""
def normal_upper_bound(p:float, mean:float=0, std_dev:float=1) ->float :
    """
    Returns z for which P(Z<=z) = probability
    """
    return normal_icdf(p,mean,std_dev)

def normal_lower_bound(p:float, mean:float=0, std_dev:float=1) ->float :
    """
    Returns z for which P(Z>=z) = probability
    """
    return normal_icdf(1-p,mean,std_dev)

def normal_twosided_bounds(p:float, mean:float=0, std_dev:float=1) ->Tuple[float,float] :
    """
    Returns symmetric bounds about the mean that contain the specified probability
    """
    tail_p = (1-p)/2
    #Upper bound should have tail probability above it
    upper_bound = normal_lower_bound(tail_p,mean,std_dev)
    #Lower bound should have tail probability below it
    lower_bound = normal_upper_bound(tail_p,mean,std_dev)
    return lower_bound,upper_bound

"""
Consider a 1000 flips of a coin (n=1000). If out hypothesis is true, X should be distributed normally with mean=500 and standard deviation=15.811
"""
def main() :
    p=0.5
    n=1000
    mean_H0, std_dev_H0 = normal_approximation_to_binomial(n, p)
    #print(f"Mean = {mean_H0}, Standard Deviation = {std_dev_H0}")

    """
    Significance - How willing we are to make a Type 1 Error("False Positive") - We reject H0 even if it is true. Generally set to 1% or 5%.
    """
    #Type 1 Error = 5%
    lower_bound5, upper_bound5 = normal_twosided_bounds(1-0.05, mean_H0, std_dev_H0)
    print(f"For Type 1 Error = 5%, lower and upper bounds are : {lower_bound5:.2f}, {upper_bound5:.2f}")

    #Type 1 Error = 1%
    lower_bound1, upper_bound1 = normal_twosided_bounds(1-0.01, mean_H0, std_dev_H0)
    print(f"For Type 1 Error = 1%, lower and upper bounds are : {lower_bound1:.2f}, {upper_bound1:.2f}")

    """
    Power of a test - Probability of not making a Type 2 Error ("false negative") in which we fail to reject H0 when it is false. To measure this we need to specify exactly what H0 being False means.
    Knowing p!=0.5 is vague for the Type 2 Error computation.
    Consider p=0.55
    """
    #Type 1 Error = 5%
    #Bounds based on assumption that p=0.5 and type1 error is 5%
    lower_bound5, upper_bound5 = normal_twosided_bounds(1-0.05, mean_H0, std_dev_H0)
    #mean and std_dev for actual value of p=0.55
    n=1000
    p=0.55
    mean, std_dev = normal_approximation_to_binomial(n,p)
    #Type 2 error probability
    type2err_p = normal_probability_between(lower_bound5, upper_bound5, mean, std_dev)
    power = 1-type2err_p

    print(f"Power of test (for Type 1 Error = 5%) = {power}")

    #Type 1 Error = 1%
    lower_bound1, upper_bound1 = normal_twosided_bounds(1-0.01, mean_H0, std_dev_H0)
    #mean and std_dev for actual value of p=0.55
    n=1000
    p=0.55
    mean, std_dev = normal_approximation_to_binomial(n,p)
    #Type 2 error probability
    type2err_p = normal_probability_between(lower_bound1, upper_bound1, mean, std_dev)
    power = 1-type2err_p

    print(f"Power of test (for Type 1 Error = 1%) = {power}")

if __name__ == "__main__" :
    main()
