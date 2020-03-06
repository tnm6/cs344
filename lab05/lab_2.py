'''
Implementation of Bayesian network to model a cancer domain with probability
of cancer and the positive or negative results of two tests

Completed for Lab 5, CS-344, Professor Vander Linden, Calvin University
@author Nathan Meyer (tnm6)
@date   6mar2020
'''

from probability import BayesNet, enumeration_ask

# Utility Variables
T, F = True, False

cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2})
])

# Compute P(Cancer | Test1 ^ Test2)
print('P(Cancer | Test1 ^ Test2):')
print('\t' + enumeration_ask('Cancer', dict(
    Test1=T, Test2=T), cancer).show_approx())

# Compute P(Cancer | Test1 ^ ¬Test2)
print('P(Cancer | Test1 ^ ¬Test2):')
print('\t' + enumeration_ask('Cancer', dict(
    Test1=T, Test2=F), cancer).show_approx())
