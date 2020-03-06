'''
Implementation of Bayesian network to model a happiness domain based on either
the presence of the sun or raise in pay.

Exercise 5.3
Completed for Lab 5, CS-344, Professor Vander Linden, Calvin University
@author Nathan Meyer (tnm6)
@date   6mar2020
'''

from probability import BayesNet, enumeration_ask

# Utility Variables
T, F = True, False

happiness = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
])

# Compute P(Raise | Sunny)
print('P(Raise | Sunny):')
print('\t' + enumeration_ask('Raise', dict(
    Sunny=T), happiness).show_approx())
# Result: False: 0.99, True: 0.01 (?!?!?)

# Compute P(Raise | Happy ^ Sunny)
print('P(Raise | Happy ^ Sunny):')
print('\t' + enumeration_ask('Raise', dict(
    Happy=T, Sunny=T), happiness).show_approx())
# Result: False: 0.986, True: 0.0142

'''
  These results are a bit perplexing, mostly because, at least by my own reason
(that's dangerous enough), being sunny wouldn't affect the chance of a raise.
The Bayesian network suggests that they are independent of each other, but I
suppose the small (1%) probability of a raise is taking into account the
(maybe) coincidental correlation that a raise occured on the same day? But that
is not the probability being calculated...

P(Raise | Sunny) = α <P(Raise | Sunny), P(¬Raise | Sunny)>
= α <( P(Sunny | Raise) * P(Raise) ), ( P(Sunny | ¬Raise) * P(¬Raise) )>
= 
'''
