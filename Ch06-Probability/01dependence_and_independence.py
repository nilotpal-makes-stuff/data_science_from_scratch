#01conditional_probability.py

"""
+--------------+
| Introduction |
+--------------+
Probability is a way of quantifying the uncertainity associated with events chosen from some universe of events.
Notationally P(E) means probability of some event E.
We use probability theory to build models and evaluate models.

+-----------------------------+
| Dependence and Independence |
+-----------------------------+
We say that two events A and B are 'dependent' if knowing something about whether A happens gives us information about whether B happens and vice versa.
If the knowledge about whether event A happens doesn't give us any information regarding whether event B happens, then we can say that events A and B are independent.

Example :
    * Flipping coin twice - the result of first flip (event A) doesn't tell us anything about the next flip (event B) - independent events.
    * Flipping coin twice and getting two heads while first flip is known - first flip(event A) determines whether we will get two heads on flipping coin twice(event B) - dependent events.

Mathematically if two events A and B are independent, then the probability that both the events happen is equal to the product of their individual probabilities.
    P(A,B) = P(A)*P(B)
"""

