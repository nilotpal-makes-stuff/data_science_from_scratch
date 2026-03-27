#04pHacking.py

"""
+-----------+
| p-Hacking |
+-----------+
For 95% confidence, the procedure erroneously rejects the null hypothesis 5% of the time.
"""
from typing import List
import random

def run_experiment(p:float, n:int) -> List[bool] :
    """
    For an experiment with binary output, conduct experiment 'n' times with success probability 'p' and return list of boolean values.
    True if experiment was a success, False otherwise.
    """
    return [random.random() < p for _ in range(n)]

def reject_fairness(experiment:List[bool], conf_int:[float,float]) -> bool :
    """
    Check if number of successes is in Confidence Interval
    """
    num_success = sum(experiment)
    return num_success < conf_int[0] or num_success > conf_int[1]

#Consider coin flip experiment - fair coin has chance of head, p=0.5. Flipping a coin 1000 times.
n=1000
p=0.5

#Number of times to conduct experiment
num_exp = 1000

#Confidence interval can be obtained using normal_two_sided_bounds(0.95, mean, std_dev) for fair coin
conf_int = [469, 531]
experiments = [run_experiment(p,n) for _ in range(num_exp)]
#print(experiments)
rejections = [reject_fairness(exp,conf_int) for exp in experiments]
#print(rejections)
#Count of rejections
num_rej = sum(rejections)
print(f"Number of experiments not within Confidence Interval = {num_rej}")
print(f"Percentage of rejections = {num_rej/num_exp*100}%")

"""
Number of rejections should be lower than 5% of total experiments done.
This means that if we set out to find "significant" results, we will usually find them.
If we test enough hypotheses against dataset, one of them will almost certainly appear significant. Removing the correct outliers will also get p-value below 0.05 (5%).
This is called p-hacking and is a consequence of the "inference from p-values framework".

To perform good science,
    * determine hypotheses before looking at data
    * clean data without hypotheses in mind
p-values are not substitutes for common sense.
"""
