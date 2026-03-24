#03BayesTheorem.py

"""
+---------------+
| Bayes Theorem |
+---------------+
Bayes theorem is a way of reversing conditional probabilities. To know the probability of an event A happening given that an event B has occured (P(A|B)), we can use the probability of an event B happening given that event A has occured (P(B|A)) and the probability of event B happening (P(B)).

Since
    P(A|B) = P(A,B)/P(B)
Similarly
    P(B|A) = P(B,A)/P(A)
Now
    P(B,A) = P(A,B) = Probability of events A and B happening
Thus
    P(A|B) = P(B|A)*P(A)/P(B)
This is Bayes theorem.

Law of total probability states that if events A1, A2, ...An are mutually exclusive and exhaustive, then
    P(B) = sum(P(B|Ai) * P(Ai))
Mutually Exclusive events - events which cannot occur at the same time
Exhaustive events - A set of events is exhaustive if at least one of them must occur whenever the experiment is performed
Using the above rule :
    P(B) = P(B|A)*P(A) + P(B|not A)*P(not A)
Thus, Bayes theorem becomes :
    P(A|B) = P(B|A)*P(A)/(P(B|A)*P(A) + P(B|not A)*P(not A))
"""

"""
Example problem :
A disease affects 1 in 10000 people. Accuracy of a test for the disease is 99%. Find the probability that a subject has the disease provided the test came back positive.

Solution :
disease affects 1 in 10000 people :
    P(D) = 1/10000
    P(not D) = 9999/10000
Accuracy of a test for the disease is 99% :
    P(T|D) = 99/100
    P(T|not D) = 1/100
probability that a subject has the disease provided the test came back positive :
    P(D|T) = P(T|D)*P(D)/(P(T|D)*P(D) + P(T|not D)*P(not D))
    P(D|T) = (99/100)*(1/10000)/((99/100)*(1/10000) + (1/100)*(9999/10000))
    =0.98%
"""
p_dt = (99/100)*(1/10000)/((99/100)*(1/10000) + (1/100)*(9999/10000))
print(f"Probability that a person has disease provided the test comes back positive = {p_dt*100:.2f}%")
print()
"""
Imagine 1 million people(1000000) take the test.
1 out of 10000 have the disease - 0.01%.
"""
people = 1000000
diseased = people * 1/10000
healthy = people-diseased
print(f"Total people : {people}\nDiseased people : {diseased}\nHealthy people : {healthy}\n")
"""
Out of diseased people 99% will receive positive result since test accuracy is 99%
Out of healthy people 1% will receive positive result since test accuracy is 99%
"""
positive_diseased = diseased* 0.99
positive_notdiseased = healthy * 0.01
print(f"People with disease tested positive : {positive_diseased}\nPeople without disease tested positive : {positive_notdiseased}\n")
"""
Percent of people who got positive test result who actually have the disease = people who have disease who tested positive/ all people who tested positive
"""
total_positive = positive_diseased + positive_notdiseased
print(f"Percent of people who tested positive and actually have disease : {positive_diseased/total_positive * 100 :.4f}%")

"""
The above example assumes that people take the test at random i.e., people who donot show symtoms are also taking test. If only people with certain symtoms accurate to the disease take test, we will then use conditional probability on event "Positive test and shows symtoms" - giving us a higher value for total positive.
"""
