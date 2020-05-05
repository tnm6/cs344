/**
 * Exercise 12.2 for CS-344, Professor Keith VanderLinden, Calvin University
 * Answers by Nathan Meyer (tnm6)
 */

% a. From LPN!
%   i.  Exercise 2.1
/**
 * 1 unifies because of clause 1, so the answer is simply yes
 * 2 does not unify because of clause 1
 * 8 unifies, X is instantiated to bread
 * 9 unifies, X is instantiated to sausage and Y is instantiated to bread
 * 14 does not unify, X is first instantiated to drink(beer) and cannot be re-
 *  instantiated to food(bread)
 */

%   ii. Exercise 2.2
house_elf(dobby). 
witch(hermione). 
witch('McGonagall').
witch(rita_skeeter). 
magic(X):-  house_elf(X). 
% magic(X):-  wizard(X).
magic(X):-  witch(X).

% ?- magic(house_elf).
% ?- wizard(harry).
% ?- magic(wizard).
% ?- magic('McGonagall').
% ?- magic(Hermione).