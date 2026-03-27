#05Example-Running_an_AB_Test.py

"""
+------------------------------+
| Example - Running an AB Test |
+------------------------------+
Consider independent experiments A and B with probabilities of success p(A) and p(B) respectively.
If the difference between p(A) and p(B) is not large or significant enough we use statistical inference to understand the significance of probabilities obtained.

Let number of trials of experiment A be 'Na' and number of successes be 'na', number of trials of experiment B be 'Nb' and number of successes be 'nb'.
If each trial in experiment A and B is independent, we can think of each trial as a Bernoulli Trial with probabilities of success pa = na/Na and pb = nb/Nb.
If values of Na and Nb are large enough, we can assume that na/Na and nb/Nb are normal variables with means pa and pb respectively and standard deviations sqrt(pa*(1-pa)/Na) and sqrt(pb*(1-pb)/Nb) respectively.
"""
from typing import Tuple
import math

def est_params(N:int, n:int) -> Tuple[float,float] :
    """
    For experiment with N independent trials and n successes, return mean and standard deviation
    """
    p=n/N
    std_dev = math.sqrt(p*(1-p)/N)
    return p,std_dev

"""
Assume both normals are independent - difference should also be normal with mean = pb-pa and standard deviation = sqrt(std_dev_a^2 + std_dev_b^2)

NOTE : This math works only if we know the standard deviations of both experiments beforehand. Estimating standard deviations from data requires us to use the T-distribution.
For large enough datasets the result is close enough and does not make much of a difference

Null hypothesis : pa and pb are the same i.e., pa-pb = 0
"""

def ab_test_stat(Na:int, na:int, Nb:int, nb:int) -> float :
    """
    Return the test statistic for A/B Test.
    Null hypothesis : pa and pb are same (pa-pb = 0)
    """
    pa, sd_a = est_params(Na,na)
    pb, sd_b = est_params(Nb,nb)
    z = (pb-pa)/math.sqrt(sd_a**2 + sd_b**2)
    return z

"""
This should be approximately standard normal.
Consider A with 1000 attempts and 200 successes, B with 1000 attempts and 180 successes.
"""
Na = 1000
na = 200
Nb = 1000
nb = 180

z = ab_test_stat(Na,na,Nb,nb)
print(f"Experiment A parameters :\nNumber of attempts (Experiment A) = {Na}\nNumber of successes (Experiment A) = {na}\nNumber of attempts (Experiment B) = {Nb}\nNumber of successes (Experiment B) = {nb}\nA/B test statistic : {z:.2f}\nTwo sided pvalue = 0.254\n")

"""
Two sided p value is obtained using function two_sided_p_value() from pervious chapter. It is the probability of seeing such a difference in between the two means if both means were equal.

0.254 translates to 25% - large enough that we cannot conclude that there is large difference between the two.

Consider A with 1000 attempts and 200 successes, B with 1000 attempts and 150 successes.
"""

Na = 1000
na = 200
Nb = 1000
nb = 150

z = ab_test_stat(Na,na,Nb,nb)
z = ab_test_stat(Na,na,Nb,nb)
print(f"Experiment A parameters :\nNumber of attempts (Experiment A) = {Na}\nNumber of successes (Experiment A) = {na}\nNumber of attempts (Experiment B) = {Nb}\nNumber of successes (Experiment B) = {nb}\nA/B test statistic : {z:.2f}\nTwo sided pvalue = 0.003\n")

"""
0.003 translates to 0.3% probability that we will see a large difference if the means of A and B were equal i.e., if both A and B experiments had equal results.
"""
