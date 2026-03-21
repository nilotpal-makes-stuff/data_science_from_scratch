#03Dispersion.py

"""
Dispersion measures how spread out our data is i.e., they are statistics for which values near zero signify that values are not spread out at all while values which are large signify that values are very spread out.
A simple measure of dispersion is the 'range' which gives us the difference between the largest and the smallest values in a collection of values.
"""
from typing import List

def data_range(values:List[float]) -> float :
    """
    Returns 'range' of a collection of values
    """
    return (max(values)-min(values))

"""
Range is zero when both maximum and minimum of the collection is equal - This happens only if all values in the collection are equal or the collection contains only one value.
Range doesn't depend on the values in the collection, it only depends on the maximum and minimum values of the collection.

A more complex meaure of spread is the 'variance'.
In probability theory and statistics, 'variance' is the expected value of the squared deviation from the mean of a random variable.
It is calculated as the average of the squared differences of each element from the mean.

NOTE :
* The variance value calculated here is the variance of a collection of equally likely values.
* For variance calculation we consider the size as size-1 (Sample population). This is done to reduce bias due to the mean value.
"""
def variance(values:List[float]) -> float :
    """
    Returns the average variance value for the entire collection of values
    """
    size = len(values)
    if size < 2 :
        raise Exception("[ERROR] We need atleast 2 elements to determine variance.")

    mean = sum(values)/size
    #Compute difference from mean for each element
    temp_list = [i-mean for i in values]
    #Compute square of differences from the mean for each element
    temp_list = [i**2 for i in temp_list]
    #Variance is the average of squared difference from the mean for each element
    return (sum(temp_list)/(size-1))

"""
When we deal with samples from a larger population, the mean is actually an estimate and not the real mean. To counter this we use the (n-1) value for calculating the variance value. This is called Bessel's Correction.

Since the result of variance gives square units (if elements are weights(kg) then variance unit is weights squared(kg^2)), we use the square root value of variance to make sense of the spread. This is called the standard deviation.
"""
import math

def standard_deviation(values:List[float]) -> float :
    """
    Return standard deviation of the list
    """
    var = variance(values)
    return math.sqrt(var)

"""
Both 'range' and 'standard deviation' have the same outlier problem - outliers can cause misleading insights from range and standard deviation values.

We can alternatively use the 'Interquartile Range' - it is the difference between the 75th percentile and the 25th percentile value. This is unaffected by the outliers if the number of outliers in data is small.
"""
def interquartile_range(values:List[float]) -> float :
    """
    Return the interquartile range of the list
    """
    size = len(values)
    values_sorted = sorted(values)
    third_quartile = values_sorted[int(size * 0.75)]
    first_quartile = values_sorted[int(size * 0.25)]
    return third_quartile-first_quartile

import random

random.seed(1)
arr = [random.randint(1,100) for _ in range(100)]
print(f"array : {arr}")
print(f"Range : {data_range(arr)}")
print(f"Interquartile range : {interquartile_range(arr)}")
print(f"Mean : {sum(arr)/len(arr)}")
print(f"Variance : {variance(arr)}")
print(f"Standard deviation : {standard_deviation(arr)}")


