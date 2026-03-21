#02Central_tendencies.py

"""
+--------------------+
| Central Tendencies |
+--------------------+
"""
import random

height_rng = (150,190)
#Generate random heights in centimeters(cm)
random.seed(12)
heights = [random.random() for _ in range(100)]
heights = [int(h*(height_rng[1]-height_rng[0])+height_rng[0]) for h in heights]
print(f"Heights data : {heights}")

"""
We may want some notion of where our data is centered.
Simplest central tendency is the average value or the mean value which is the sum of all values divided by the number of values
"""
from typing import List
def mean(values:List[float]) -> float :
    return sum(values)/len(values)

print(f"Average value : {mean(heights)}")

"""
Mean of a group of values depends on each value in the group.

Another central tendency is the 'Median' which represents the middle most value(for a collection of values having odd count) or the average of the two middle values(for a collection of values having even count).
The median does not depend on every value in the collection of values, it only depends on the middle values.
"""
def median(values:List[float]) -> float :
    """
    Return median value for a collection
    """
    values_sorted = sorted(values)
    #if count is odd
    if len(values)%2 == 1 :
        return values_sorted[len(values_sorted)//2]
    else :
        median = (values_sorted[len(values_sorted)//2] + values_sorted[(len(values_sorted)//2)-1])/2
        return median

assert median([1,2,3,4,5]) == 3
assert median([1,2,3,4]) == 2.5
assert median([1,2,3,4,5,6]) == 3.5

"""
Mean is simpler to compute and it varies smoothly as the data changes. For 'n' data points if one value increases by some amount 'e' then the mean value will incerase by "e/n".

To find the median value we need to sort the data - can be expensive for large datasets.
We can also efficiently compute median without sorting the data - https://en.wikipedia.org/wiki/Quickselect

Mean is sensitive to outliers in data. If outliers are likely to be bad data or are otherwise data unrepresentative of the phenomenon we are trying to understand then the "mean" can provide a misleading picture.

Use both mean and median in conjunction to understand data and help detect outliers.

A generalization of the median is the "quantile" which represents the value under which a certain percentile of the data lies. The median represents the value undere which 50% of the data lies.
"""

def quantile(values:List[float], p:float) -> float :
    """
    Returns the p-th percentile value in collection of values 'values'
    """
    #Using median() for p=0.5 i.e., 50%
    if p==0.5 :
        return median(values)
    p_index = int(p*len(values))
    return sorted(values)[p_index]

print(quantile([1,2,3,4,5], 0.5))
print(quantile([1,2,3,4], 0.5))
print(quantile([1,2,3,4,5,6], 0.33))

"""
Mode is another central tendency which represents the most common value in a collection of values.
For a collection of values there can be multiple modes.
"""
from collections import Counter
def mode(values:List[float]) -> List[float] :
    """
    Returns the mode or modes of a collection of values(list of floats)
    """
    counts = Counter(values)
    max_items = max(counts.values())
    return [i for i,count in counts.items() if count==max_items]

print(mode(heights))
