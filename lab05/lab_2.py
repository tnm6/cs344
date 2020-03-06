'''
Implementation of Bayesian network to model a cancer domain with probability
of cancer and the positive or negative results of two tests

Exercise 5.2
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
# Result: False: 0.83, True: 0.17

# Compute P(Cancer | Test1 ^ ¬Test2)
print('P(Cancer | Test1 ^ ¬Test2):')
print('\t' + enumeration_ask('Cancer', dict(
    Test1=T, Test2=F), cancer).show_approx())
# Result: False: 0.994, True: 0.00565

'''
  These results are unsurprising. Given the low probability of actually having
cancer (1%), even a relatively accurate test(s) for those who have cancer will
not very reliably (in this calculation, 17%) determine the diagnosis on its own
  Then, if one test is negative, it makes sense that the probability of having
cancer worsens dramatically as well.

Hand calculations (distribution of <true, false>):
P(Cancer | Test1 ^ Test2) = α <P(Cancer | Test1 ^ Test2), P(¬Cancer | Test1 ^ Test2)
= α <( P(Test1 | Cancer) * P(Test2 | Cancer) * P(Cancer) ), ( P(Test1 | ¬Cancer) * P(Test2 | ¬Cancer) * P(¬Cancer) )>
= α <(0.9 * 0.9 * 0.01), (0.2 * 0.2 * (1 - 0.01))> = α <0.0081, 0.0396> = (approx) 21 * <0.0081, 0.0396>
~= <0.17, 0.83>

P(Cancer | Test1 ^ ¬Test2) = α <P(Cancer | Test1 ^ ¬Test2), P(¬Cancer | Test1 ^ ¬Test2)
= α <( P(Test1 | Cancer) * P(¬Test2 | Cancer) * P(Cancer) ), ( P(Test1 | ¬Cancer) * P(¬Test2 | ¬Cancer) * P(¬Cancer) )>
= α <(0.9 * (1 - 0.9) * 0.01), (0.2 * (1 - 0.2) * 0.99)> = α <0.0009, 0.1584> = (approx) 6.28 * <0.0009, 0.1584>
= <0.006, 0.994>

  Based on these hand calculations, the computations are accurate, further
verifying that the rarity of cancer significantly affects how reliable the test
results are in diagnosing cancer.
'''
