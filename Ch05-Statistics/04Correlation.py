#04Correlation.py

"""
+------------+
| Covariance |
+------------+
Covariance is the paired analogue of variance, it measures how two variables vary in tandem from their means. It is calculated as the dot product of vectors containing the deviation of each element from mean value for both variables divided by the number of elements -1 (-1 to correct for bias)
"""

#Dot product of two vectors is the sum of their componentwise products
def dot(vec1:Vector, vec2:Vector) -> float :
    """
    Compute Dot porduct of two vectors.
    """
    if len(vec1) != len(vec2) :
        raise Exception("[ERROR]Vectors are not of the same size.")
    result = [i*j for i,j in zip(vec1,vec2)]
    result = sum(result)
    return result

#covariance for two vectors
def covariance(vec1:Vector, vec2:Vector) -> float :
    """
    Compute the covariance of two vectors
    """
    if len(vec1) != len(vec2) :
        raise Exception("[ERROR]Vectors are not of the same size.")

    #Mean values for vectors
    mean1 = sum(vec1)/len(vec1)
    mean2 = sum(vec2)/len(vec2)

    #Deviation vectors for each vector
    vec1_de = [i-mean1 for i in vec1]
    vec2_de = [i-mean2 for i in vec2]

    return dot(vec1_de, vec2_de)/(len(vec1)-1)

"""
+--------------------------+
| Understanding Covariance |
+--------------------------+
Consider two vectors A and B.
Dot product sums up the products of the deviations for corresponding elements.
If the corresponding elements in vectors A and B are both above their respective mean values or are both below their respective mean values, a positive number enters the sum for calculating covariance.
If the element in vector A is above the mean value while the element in vector B is below the mean value or vice versa, a negative number enters the sum for calculating covariance.

Thus if covariance value is a large positive number:
    * The values in vector A are large if the values in vector B are large
    * The values in vector A are small if the values in vector B are small

If covariance value is a large negative number:
    * The values in vector A are small if values in vector B are large
    * The values in vector A are large if values in vector B are small

If covariance value is small(near zero) :
    * The values in the two vectors are not related i.e., donot influence each other.

The unit of measurement for a covariance between two vectors is the product of units for each vector. This makes it hard to make sense of the covariance value obtained. It is also hard to define what is a 'large' value for covariance.

+-------------+
| Correlation |
+-------------+
Due to the shortcomings of the covariance value, we compute the 'Correlation' value between two vectors. In statistics correlation refers to the degree to which a pair of variables are linearly related.
Its values are in the range [-1, 1] where -1 indicates that the variables are anti-correlated while 1 indicates that the variables are correlated. 0 indicates that the variables are not related.

Correlation is computed as the result of dividing covariance with the product of standard deviations of each vector. Correlation is unitless.
"""
#variance
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

import math
#Standard deviation
def standard_deviation(values:List[float]) -> float :
    """
    Return standard deviation of the list
    """
    var = variance(values)
    return math.sqrt(var)

#correlation for two vectors
def correlation(vec1:Vector, vec2:Vector) -> float :
    """
    Compute the covariance of two vectors
    """
    if len(vec1) != len(vec2) :
        raise Exception("[ERROR]Vectors are not of the same size.")

    #covariance
    covar = covariance(vec1, vec2)

    #Standard Deviation
    sd_vec1 = standard_deviation(vec1)
    sd_vec2 = standard_deviation(vec2)

    return covar/(sd_vec1*sd_vec2)

#Test covariance and correlation
import random

def main() :
    random.seed(1)
    arr1 = [random.randint(0,100) for _ in range(100)]
    arr2 = [random.randint(0,100) for _ in range(100)]
    print(f"Arrays : \n{arr1}\n{arr2}")
    print(f"Covariance : {covariance(arr1, arr2)}")
    print(f"Correlation : {correlation(arr1, arr2)}")

if __name__ == "__main__" :
    main()
"""
NOTE : Correlation is very sensitive to outliers. Without outliers in the data we can get an accurate sense of how correlated the two variables are. Plot out the data for both variables to help identify outliers which can then be removed from the correlation calculation to get a more accurate sense of the correlation between the two variables.
"""
