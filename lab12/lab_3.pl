/**
 * Exercise 12.3 for CS-344, Professor Keith VanderLinden, Calvin University
 * Answers by Nathan Meyer (tnm6)
 */

% Monty Python "She's a witch!" skit in logic form
witch(X):- burns(X).
burns(X):- made_of_wood(X).
made_of_wood(X):- floats(X).
floats(X):- same_weight(X, duck).
same_weight(woman, duck).

?- witch(woman).
% Returns true.