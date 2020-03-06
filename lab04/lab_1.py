'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013

Added computations for Exercise 4.1 of Lab 4
@author: Nathan Meyer (tnm6)
@date 5mar2020
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print(PC.show_approx())

# Compute P(Cavity|Catch=T)
'''
Hand calculated P(Cavity|Catch=T)
P(Cavity|Catch) = P(Cavity, Catch) / P(Catch) (Bayes' Rule)
= (0.108 + 0.072) / (0.108 + 0.072 + 0.016 + 0.144)
= 0.529
So hand calculation is: False: 0.471, True: 0.529
'''
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC.show_approx())

# Computation result is: False: 0.471, True: 0.529

# Joint Probability Distribution for flipping two coins
P = JointProbDist(['Coin1', 'Coin2'])
H, T = 'Heads', 'Tails'
P[H, H] = 0.25; P[H, T] = 0.25
P[T, H] = 0.25; P[T, T] = 0.25

# Compute P(Coin2|Coin1=Heads)
PC = enumerate_joint_ask('Coin2', {'Coin1': T}, P)
print(PC.show_approx())

# Computation result: Heads: 0.5, Tails: 0.5
# This is what I expected, since flipping each coin is
# independent of the other coinflip, i.e. each is 0.5

