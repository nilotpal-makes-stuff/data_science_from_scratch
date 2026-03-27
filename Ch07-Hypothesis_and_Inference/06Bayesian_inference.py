#06Bayesian_inference.py

"""
+--------------------+
| Bayesian Inference |
+--------------------+

"""
import matplotlib.pyplot as pyplot
import math

def B(alpha:float, beta:float) -> float:
    """
    Normalizing constant to make total probability = 1
    """
    return math.gamma(alpha)*math.gamma(beta)/math.gamma(alpha+beta)

def beta_pdf(x:float, alpha:float, beta:float) -> float :
    """
    Beta distribution Probability Distribution function
        x^(alpha-1) * (1-x)^(beta-1) / B(alpha,beta)
    """
    #No weight outside [0,1]
    if x <=0 or x >=1 :
        return 0
    val = (x**(alpha-1) * (1-x)**(beta-1))/B(alpha, beta)
    return val
#
resolution = 100

xaxis = [i/resolution for i in range(resolution)]

#alpha = 1, beta = 1
alpha,beta = 1,1
yaxis = [beta_pdf(x,alpha,beta) for x in xaxis]
pyplot.plot(xaxis, yaxis, color='black', label='Beta(1,1)')

#alpha = 10, beta = 10
alpha,beta = 10,10
yaxis = [beta_pdf(x,alpha,beta) for x in xaxis]
pyplot.plot(xaxis, yaxis, color='green', label='Beta(10,10)')

#alpha = 4, beta = 16
alpha,beta = 4,16
yaxis = [beta_pdf(x,alpha,beta) for x in xaxis]
pyplot.plot(xaxis, yaxis, linestyle='--', color='red', label='Beta(4,16)')

#alpha = 4, beta = 6
alpha,beta = 4,6
yaxis = [beta_pdf(x,alpha,beta) for x in xaxis]
pyplot.plot(xaxis, yaxis, linestyle='--', color='green', label='Beta(4,6)')

#alpha = 16, beta = 4
alpha,beta = 16,4
yaxis = [beta_pdf(x,alpha,beta) for x in xaxis]
pyplot.plot(xaxis, yaxis, linestyle='-.', color='blue', label='Beta(16,4)')

#alpha = 6, beta = 4
alpha,beta = 6,4
yaxis = [beta_pdf(x,alpha,beta) for x in xaxis]
pyplot.plot(xaxis, yaxis, linestyle='--', color='blue', label='Beta(6,4)')

#yaxis adjust
pyplot.ylim(0,6)

#Display plot
pyplot.title("Example Beta Distributions")
pyplot.legend()
pyplot.show()

"""
For equal values of alpha and beta, the distribution is centered at 0.5.
For alpha = beta = 1, the distribution is centered at 0.5 and is very dispersed

For alpha > beta, the distribution is more weighted towards 1.
For alpha < beta, the distribution is more weighted towards 0.

Lets assume a prior distribution on p for a coin flip :
    * Not taking a stand on whether coin is fair - uniform prior - alpha=1, beta=1
    * Strong belief that coin is biased - lands 55% heads - alpha=55, beta=45

If we perform experiment N times and get h heads and t tails, Bayes theorem talls us that posterior distribution for p is a Beta Distribution with parameters alpha=alpha+h, beta=beta+t

NOTE : Beta distribution is conjugate prior to Binomial distribution. When we update Beta prior using observations from the corresponding binomial, we get back a Beta posterior.

Consider example of coin flip 10 times with 3 heads.
For Uniform prior Beta(1,1), Posterior distribution is Beta(4,7) :

"""
from typing import Tuple

def coinflip(num_trials:int, num_heads:int, resolution:int, prior_dist:Tuple[int,int]) -> None :
    """
    Display prior distribution vs posterior distribution for a coinflip
    """
    alpha,beta = prior_dist
    xaxis = [i/resolution for i in range(resolution)]
    yaxis = [beta_pdf(x,alpha,beta) for x in xaxis]
    pyplot.plot(xaxis, yaxis, color='red', label=f"Prior Distribution = Beta({alpha},{beta})")
    #mark center
    sorted_y = dict(sorted(dict(enumerate(yaxis)).items(), key=lambda item: item[1], reverse=True))
    peak =  next(iter(sorted_y.items()))[0]
    pyplot.axvline(x=xaxis[peak], color='red', linestyle='--', label=f"Center p={xaxis[peak]}")

    alpha,beta = alpha+num_heads, beta+(num_trials-num_heads)
    yaxis = [beta_pdf(x,alpha,beta) for x in xaxis]
    pyplot.plot(xaxis, yaxis, color='green', label=f"Posterior Distribution = Beta({alpha},{beta})")
    #mark center
    sorted_y = dict(sorted(dict(enumerate(yaxis)).items(), key=lambda item: item[1], reverse=True))
    peak =  next(iter(sorted_y.items()))[0]
    pyplot.axvline(x=xaxis[peak], color='green', linestyle='--', label=f"Center p={xaxis[peak]}")

    pyplot.title("Prior vs Posterior")
    pyplot.legend()
    pyplot.show()

resolution = 100
num_tries = 10
num_heads = 3

#prior Beta(1,1)
#prior_dist = (1,1)
#coinflip(num_tries, num_heads, resolution, prior_dist)

"""
When we use prior Beta(20,20) - coin is roughly fair - posterior distribution Beta(23,27) is centered at 0.46 - coin slightly biased towards tails.
This disproves our prior assumption of coin being fair.
"""
#prior Beta(20,20)
prior_dist = (20,20)
#coinflip(num_tries, num_heads, resolution, prior_dist)

"""
When we use prior Beta(30,10) centered at 0.76 - coin is heads biased - posterior distribution Beta(33,17) is centered at 0.67 - coin bias towards head is reduced.
This makes us less strongly believe in the head bias.
"""
#prior Beta(30,10)
prior_dist = (30,10)
coinflip(num_tries, num_heads, resolution, prior_dist)

"""
If we flip coin a lot of times (large sample), the prior would matter less. Increasing sample size makes the posterior distribution to eventually become the same no matter the prior.
This allows us to make probability statements about hypotheses.

Using Bayesian inference to test hypotheses is controversial beacuse :
    * math involved can get complicated
    * subjective to the choice of the prior

Prior like Beta(10000,1) in the example above will give us wrong conclusions as prior is heavily biased to a single outcome.
"""
#prior Beta(10000,1) throws math range error
#prior Beta(100,1)
prior_dist = (100,1)
coinflip(num_tries, num_heads, resolution, prior_dist)
