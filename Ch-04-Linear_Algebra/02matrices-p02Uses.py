#02matrices-p02Uses.py

"""
+----------------+
| Matrices Usage |
+----------------+
Matrices are useful for the following reasons :
01 >    We can use a matrix to represent a dataset consisting of multiple vectors. Each row is a vector of the matrix.

02 >    We can use an nxk matrix to represent a linear function that maps k-dimensional vectors to n-dimensional vectors

03 >    We can use matrices to represent binary relationships.
For example we can store connection data between users - two users are friends then relationship=1 else 0.
This can be stored in a matrix. This approach has a drawback : huge storage required to store lots of users and their connection data. The advantage for this approach is that lookup of connections is significantly faster.
connection_matrix[userA][userB] == 1 check is faster than iterating through list of connections.
"""

"""
+---------------------+
| Further Exploration |
+---------------------+
* Linear Algebra by Jim Hefferson (https://joshua.smcvt.edu/linearalgebra)
* Linear Algebra (https://www.math.ucdavis.edu/~linear/linear-guest.pdf)
* Linear Algebra Done Wrong (https://www.math.brown.edu/~treil/papers/LADW/LADW_2017-09-04.pdf)
"""
