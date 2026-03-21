#01vectors.py

#Vectors can be thought of as points in some finite dimensional space - usefulfor representing correlated numerical data.
#Vectors are objects that can be added together or multiplied with scalars to form new vectors

#Simplest way to represent vectors is by using lists of numbers. Length of list denotes dimesions of the vector
#We can use type alias on a list of floats to represent a Vector
#We use 'List' from 'typing' module in python
from typing import List

#typing module provides support for type hints, enabling developers to annotate variables, function parameters, and return values with explicit types.
#It consists of List, Dict, Set, Tuple, Callable, Optional, Union, Any as basic types which can be used to define collections having elements of a single datatype

#Create alias for List of floats as a vector
Vector = List[float]

#Generate random height weight age values
import random
#return random value in range
def random_val(minval, maxval) :
    value = minval + random.random()*(maxval-minval)
    return int(value)

#return random height
def get_height() :
    height_range = (160, 190)
    return random_val(*height_range)

#return random height
def get_weight() :
    weight_range = (60, 90)
    return random_val(*weight_range)

#return random height
def get_age() :
    age_range = (20, 70)
    return random_val(*age_range)

#example vectors
#person - contains height(cm), weight(Kg), age(years) values
p1 = [get_height(), get_weight(), get_age()]
p2 = [get_height(), get_weight(), get_age()]

print(p1,p2)
print(type(p1), type(p2))

#We need to construct arithmetic functions for the vectors

#Vector addition - each element of vector added to corresponding element of the other vector
#Both vectors need to be of the same dimensions
def add(vec1:Vector, vec2:Vector) -> Vector :
    """
    Add two vectors and return result vector
    """
    if len(vec1) != len(vec2) :
        raise Exception("[ERROR]Vectors have different dimensions.")
    res = [i+j for i,j in zip(vec1,vec2)]
    return res

#We can use assert to verify results
assert add([1,3,5], [2,4,6]) == [3,7,11]
#Verify
combined = add(p1,p2)
print(combined)

#Vector subtraction - each element of vector subtracted from corresponding element of the other vector
#Both vectors need to be of the same dimensions
def subtract(vec1:Vector, vec2:Vector) -> Vector :
    """
    Subtract vec2 from vec1 and return result vector
    """
    if len(vec1) != len(vec2) :
        raise Exception("[ERROR]Vectors have different dimensions.")
    res = [i-j for i,j in zip(vec1,vec2)]
    return res

#We can use assert to verify results
assert subtract([1,3,5], [2,4,6]) == [-1,-1,-1]
#Verify
combined = subtract(p1,p2)
print(combined)

#Componentwise sum for a list of vectors
def sum_vectors(vectors:List[Vector]) -> Vector :
    """
    Add all vectors provided and return result vector
    """
    #Check if vector list is empty
    if not vectors :
        raise Exception("[ERROR]Vector list is empty.")

    #Check if vectors have the same size
    size = len(vectors[0])
    if not all(len(v)==size for v in vectors) :
        raise Exception("[ERROR]Vector list contains vectors of different dimensions.")

    result = [sum(vector[i] for vector in vectors) for i in range(size)]
    return result

#check using assert
assert sum_vectors([[1,0,1],[2,2,0],[3,3,3]]) == [6,5,4]

#Multiplication of vector with a scalar value
def multiply(c:float, vector:Vector) -> Vector :
    """
    Multiply vector with a scalar value and return result vector
    """
    result = [c*i for i in vector]
    return result

assert multiply(10, [2,1,3]) == [20,10,30]

#We can use multiplication and sum of all vectors to obtain a vector containing element wise average value
def average(vectors:List[Vector]) -> Vector :
    """
    Average values for each position in list of vectors
    """
    num_vectors = len(vectors)
    result = sum_vectors(vectors)
    result = multiply(1/num_vectors, result)
    return result

assert average([[1,2],[3,4],[5,6]]) == [3,4]

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

assert dot([1,2,3], [4,5,6]) == 32

#Dot product of a vector with a unit vector gives us the length of the vector in the direction of the unit vector.

#sum of squares of a vector is the cumulative sum of each element squared
def sum_squared(vector:Vector) -> float :
    """
    Return the cumulative sum of each element of the vector squared.
    """
    result = sum([i*i for i in vector])
    return result

assert sum_squared([2,2,2]) == 12

#We can compute the magnitude of a vector using the sum_squared() method
#Magintude of a vector is the square root of sum of squares of each element of vector
from math import sqrt
def magnitude(vector:Vector) -> float :
    """
    Returns the magnitude of a vector
    """
    result = sqrt(sum_squared(vector))
    return result

assert magnitude([3,4]) == 5

#distance between vectors is the square root of the sum of the squares of element wise subtraction of the vectors
def distance(vec1:Vector, vec2:Vector) -> float :
    """
    Return distance between the two vectors
    """
    result = magnitude(subtract(vec1, vec2))
    return result

