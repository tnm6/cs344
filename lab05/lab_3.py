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
# Result: False: 0.99, True: 0.01

'''
  This result makes sense. Since Raise and Sunny are independent, Raise | Sunny
is equal to Raise, which is 0.01, or 1%.

P(Raise | Sunny) = P(Raise) = <0.01, 0.99>
'''

# Compute P(Raise | Happy ^ Sunny)
print('P(Raise | Happy ^ Sunny):')
print('\t' + enumeration_ask('Raise', dict(
    Happy=T, Sunny=T), happiness).show_approx())
# Result: False: 0.986, True: 0.0142

'''
  This makes some sense as well. P(Raise | Sunny) is independent, but since
happiness is dependent on whether it is Sunny or not, and we now know that they
are Happy, it should affect the probability, even if only slightly (the
probability of a Raise is still low).

P(Raise | Happy ^ Sunny) = α <P(Raise | Happy ^ Sunny), P(¬Raise | Happy ^ Sunny)>
= α <( P(Happy | Raise ^ Sunny) * P(Sunny | Raise) * P(Raise) ), ( P(Happy | ¬Raise ^ Sunny) * P(Sunny | ¬Raise) * P(¬Raise) )>
= α <( P(Happy | Raise ^ Sunny) * P(Sunny) * P(Raise) ), ( P(Happy | ¬Raise ^ Sunny) * P(Sunny) * P(¬Raise) )>
= α <(1.0 * 0.01 * 0.7), (0.7 * 0.7 * (1 - 0.01))> = α <0.007, 0.4851>
= (approx) 2.032 * <0.007, 0.4851>
= <0.014, 0.986>
'''

# Compute P(Raise | Happy)
print('P(Raise | Happy):')
print('\t' + enumeration_ask('Raise', dict(
    Happy=T), happiness).show_approx())
# Result: False: 0.982, True: 0.0185

'''
  P(Raise | Happy) sense given the result of P(Raise | Happy ^ Sunny). While
the probability of a raise on its own is very low, being given that Happy is
true, that should affect the probability slightly since happiness is dependent
on a raise.
'''

# Compute P(Raise | Happy ^ ¬Sunny)
print('P(Raise | Happy ^ ¬Sunny):')
print('\t' + enumeration_ask('Raise', dict(
    Happy=T, Sunny=F), happiness).show_approx())
# Result: False: 0.917, True: 0.0833

'''
  For P(Raise | Happy ^ ¬Sunny), the result does not make sense to me. Since we
know that is not Sunny *and* that Happy is true, it seems that the likelihood
of a Raise should be higher, because the probability of being Happy when both
Raise and Sunny are false is much lower, 10%, than the probability of Happy
when Raise is true and Sunny is false, 90%.
'''
