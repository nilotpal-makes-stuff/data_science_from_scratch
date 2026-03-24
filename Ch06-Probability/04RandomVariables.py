#04RandomVariables.py

"""
+------------------+
| Random Variables |
+------------------+
Random variable - variable whose possible values have an associated probability distribution.
Associated probability distribution gives the probabilities that the variable realizes each of its possible values.
The expected value of a random variable is the average of its values weighted by their probabilities.
For example :
    * In a coin toss head is success then getting a head is considered 1 and tail is considered 0.
    Thus expected value E(head)= 0*0.5 + 1*0.5
    * Selecting a value from 0 to 9 (range(10) function),
    expected value E = 0.1*(0+1+2+3+4+5+6+7+8+9) = 4.5

Random variables can be conditioned on events just as other events can.
For example :
Consider two child family whose gender are not known.
    * X is random variable representing the number of children who are girls
        E(X) = 0*0.25 + 1*0.5 + 2*0.25 = 1
    * Y is random variable representing number of girls conditional on at least one of the children being a girl
        E(Y) = 1*2/3 + 2*1/3 = 4/3
"""
