#03ConfidenceIntervals.py

"""
+----------------------+
| Confidence Intervals |
+----------------------+
When testing hypotheses about probability p of an event which is a parameter of an unknown distribution, we can use a third approach which is to construct a confidence interval around the observed value of the parameter.

How confident are we about the estimate? For a known probability value 'p', the Central limit theorem states that average of the Bernoulli Variables should be approximately normal with
    mean = p
    standard deviation = sqrt(p*(1-p)/n)

Using the normal approximation we can conclude that we are 'conf_p %' confident that the interval contains the true parameter 'p'
    normal_two_sided_bounds(conf_p, mean, std_dev)
Here conf_p is the probability that the actual value of 'p' lies in the interval returned by the function normal_two_sided_bounds()

This means that if we were to repeat the experiment multiple times, the true value of p will be in observed confidence interval 95% of the time.

Consider example experiment :
Flipping a coin having unknown distribution of outcomes Head and Tail 1000 times.
If number of heads we get is 525 then :
"""
import math

head=525
n=1000

p=head/n
mean = p
std_dev = math.sqrt(p*(1-p)/1000)

#For 95% confidence in results, the confidence interval which contains true value of 'p' is
confidence_percent = 0.95
#normal_two_sided_bounds(confidence_percent, mean, std_dev)
upper_bound, lower_bound = [0.4940, 0.5560]

print(f"Number of heads = {head}\nNumber of coin flips = {n}\nMean = {mean}\nStandard Deviation = {std_dev}\nConfidence Interval for the experiment with {confidence_percent*100}% Confidence : {[upper_bound,lower_bound]}")
print()
"""
Since true probability p = 0.5 (probability for a perfectly fair coin) falls in between confidence interval, we can conclude that the coin is fair.

If number of heads was 540 :
"""
head=540
n=1000

p=head/n
mean = p
std_dev = math.sqrt(p*(1-p)/1000)

#For 95% confidence in results, the confidence interval which contains true value of 'p' is
confidence_percent = 0.95
#normal_two_sided_bounds(confidence_percent, mean, std_dev)
upper_bound, lower_bound = [0.5091, 0.5709]
print(f"Number of heads = {head}\nNumber of coin flips = {n}\nMean = {mean}\nStandard Deviation = {std_dev}\nConfidence Interval for the experiment with {confidence_percent*100}% Confidence : {[upper_bound,lower_bound]}")
print()
"""
Since true probability p = 0.5 (probability for a perfectly fair coin) does not fall in between confidence interval, we can conclude that the coin is unfair.
"""
