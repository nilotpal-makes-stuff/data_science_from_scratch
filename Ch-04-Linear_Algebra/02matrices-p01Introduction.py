#02matrices-p01Introduction.py

"""
Matrices are two dimensional collection of numbers.
We can represent a matrix in the simplest form using a list of lists with each inner list having the same size and representing a row of the matrix.
"""
from typing import List

#using alias to represent Vector
Vector = List[float]
#using alias to represent type Matrix
Matrix = List[List[float]]

A = [
    [1,2,3,4],
    [5,6,7,8]
     ]

B = [
    [1,2],
    [3,4],
    [5,6]
    ]

from typing import Tuple

def shape(A:Matrix) -> Tuple[int,int] :
    """
    Shape of a matrix represents the number of rows and the number of columns of a matrix.
    This function returns the number of rows, number of columns of the matrix
    """
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

assert shape([]) == (0,0)
assert shape([[]]) == (1,0)
assert shape([[1,2],[3,4],[5,6]]) == (3,2)

"""
For a matrix with 'n' rows and 'k' columns, we call it a nxk matrix.
Each row of a nxk matrix is a vector of length k.
Each column of a nxk matrix is a vector of length n.
"""
def get_row(A:Matrix, i:int) -> Vector :
    """
    Get ith row of a matrix
    """
    try :
        vector = A[i]
        return A[i]
    except IndexError :
        raise Exception(f"[ERROR] Index {i} does not exist.")

#get_row([[1,2],[3,4]], 2)
assert get_row([[1,2,3,4],[11,12,13,14],[21,22,23,24],[31,32,33,34]], 3) == [31,32,33,34]

def get_col(A:Matrix, i:int) -> Vector :
    """
    Get ith column of a matrix
    """
    try :
        vector = [row[i] for row in A]
        return vector
    except IndexError :
        raise Exception(f"[ERROR] Index {i} does not exist.")

#get_col([[1,2],[3,4]], 2)
assert get_col([[1,2,3,4],[11,12,13,14],[21,22,23,24],[31,32,33,34]], 3) == [4,14,24,34]

"""
We can create a function which takes in a matrix shape and a generator function to generate a matrix for us.
"""
from typing import Callable
#Callable format = Callable[inputtype, outputtype]
#For multiple inputs use list of input types
def make_matrix(num_rows:int, num_cols:int, gen_func: Callable[[int,int],float]) -> Matrix :
    """
    Return a 'num_rows x num_cols' Matrix using the generator function 'gen_func()'
    """
    matrix = [[gen_func(i,j) for j in range(num_cols)] for i in range(num_rows)]
    return matrix

def identity_matrix(n:int) -> Matrix :
    """
    Returns an Identity Matrix of shape (n,n)
    """
    return make_matrix(n,n, lambda i,j : 1 if i==j else 0)

print(identity_matrix(5))
