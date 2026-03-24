#02Conditional_probability.py

"""
+-------------------------+
| Conditional Probability |
+-------------------------+
If two events A and B are not independent and probability of B is not zero, then we can define the probability of event A occuring given that event B has occured as the result of dividing the probability of event A and B occuring divided by the probability of event B occuring.
    P(A|B) = P(A,B)/P(B)

This is called as conditional probability.
If events A and B are independent, then
    P(A|B) = P(A)

We can verify probability results by generating lots of outcomes using 'random'.
"""

"""
Consider a family with 2 children whose gender is unknown. If the following assumptions are true :
    * Each child is equally likely to be a boy or a girl.
        P(B)=P(G)
    * Gender of second child is independent of gender of first child.

Find out probabilities of the following :
    * both children are girls given that older child is girl
    * both children are girls given that at least one child is girl

"""
import random

kid = ("boy", "girl")

#Count of outcomes
both_girls = 0
older_girl = 0
at_least_one_girl = 0

#Run random experiment
for _ in range(10000) :
    older_kid = random.choice(kid)
    younger_kid = random.choice(kid)
    #print(older_kid, younger_kid)

    if older_kid == 'girl' :
        older_girl += 1
        at_least_one_girl += 1
    elif younger_kid == 'girl' :
        at_least_one_girl += 1

    if older_kid == 'girl' and younger_kid == 'girl' :
        both_girls += 1

print(f"Outcomes : {both_girls},{older_girl},{at_least_one_girl}")
print(f"Probability that both are girls given that older child is girl = {both_girls/older_girl}")
print(f"Probability that both are girls given that at least one child is girl = {both_girls/at_least_one_girl}")

"""
Solutions mathematically :
* both children are girls given that older child is girl
    P(bothGirls | older_girl) = P(bothGirls, older_girl)/P(older_girl)
Probability that both are girls and older child is girl is same as probability that both are girls:
    P(bothGirls, older_girl) = P(bothGirls)
Therefore
    P(bothGirls | older_girl) = P(bothGirls)/P(older_girl)
Now
    P(bothGirls) = P(G,G) = P(G)*P(G) = 0.5*0.5 = 0.25
    P(older_girl) = P(G) = 0.5
Therfore
    P(bothGirls | older_girl) = 0.25 / 0.5 = 0.5

* both children are girls given that at least one child is girl
    P(bothGirls | at_least_one_girl) = P(bothGirls, at_least_one_girl)/P(at_least_one_girl)
Probability that both are girls and at least one child is girl is same as probability that both are girls:
    P(bothGirls, at_least_one_girl) = P(bothGirls)
Therefore
    P(bothGirls | at_least_one_girl) = P(bothGirls)/P(at_least_one_girl)
Now
    P(bothGirls) = P(G)*P(G) = 0.5*0.5 = 0.25
    P(at_least_one_girl) = P(G,G) + P(B,G) + P(G,B) = 0.25 + 0.25 + 0.25 = 0.75
Therfore
    P(bothGirls | older_girl) = 0.25 / 0.75 = 0.333
"""
