#02p-Values.py

#Import python code from files not following python import file naming conventions
import importlib.util

# Specify the filename
filename = "01Statistical_Hypothesis_Testing.py"
module_name = "hypo_test"  # Choose a valid module name

# Create a module spec and load it
spec = importlib.util.spec_from_file_location(module_name, filename)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

"""
+----------+
| p-Values |
+----------+
Instead of choosing bounds based on some probability cutoff, we can compute the probability (assuming H0 is true) that we will see a value atleast as extreme as the one we actually observed.
"""
def two_sided_p_value(x:float, mean:float=0, std_dev:float=1) -> float:
    """
    How likely are we to see a value at least as extreme as x(in either direction) if our values are from an N(mean, std_dev)
    """
    if x >= mean :
        #greater than mean value, tail is everything greater than x
        return 2*module.normal_probability_above(x, mean, std_dev)
    else :
        #less than mean value, tail is everything less than x
        return 2*module.normal_probability_below(x, mean, std_dev)

import random

def main() :
    #1000 coinflips looking for heads - mean=500, standard deviation=15.8
    #To get probability for 530 heads computing p-value
    print(f"p-value = {two_sided_p_value(529.5, 500, 15.8)}")
    #We use 529.5 rather than 530 because of Continuity Correction

    #Check with an actual experiment simulation
    extreme_val_count=0
    for _ in range(1000) :
        #Count number of heads in 1000 flips
        num_heads = sum(1 if random.random()<0.5 else 0 for _ in range(1000))
        #470,530 values are extremes taken from result of normal_two_sided_bounds+1
        if num_heads >= 530 or num_heads <= 470 :
            extreme_val_count+=1

    print(f"Number of times extreme values were obtained in 1000 experiments : {extreme_val_count}")


if __name__ == "__main__" :
    main()

"""
Always make sure data is roughly normally distributed before using the "normal_probability_above()" function to compute the p-values.
If data is not normally distributed then it can be bad or biased data which can result in incorrect conclusions from hypotheses.
Plotting the data is a good start point for checking data quality.
"""
