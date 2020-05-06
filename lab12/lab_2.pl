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

?- magic(house_elf).
/**
 * Returns false. Fails to find unify the argument house_elf with arguments from
 * any facts or rules since it is only used as a functor, not an argument.
 */

?- wizard(harry).
/**
 * Throws an "undefined procedure" error. Fails to find the functor wizard/1.
 */

?- magic(wizard).
/**
 * Throws an undefined procedure error if magic(X):- wizard(X) is defined as a
 * rule at any point. Both of the other magic/1 rules will fail, so the error
 * isn't avoidable unless the offending rule is commented out or removed.
 * 
 * Returns false. The magic functor is defined in two rules, so it unifies the
 * X in each rule to wizard, but it fails to unify this with any fact or rule
 * where house_elf/1 or witch/1 define wizard as an argument.
 */

?- magic('McGonagall').
/**
 * Before running this query, the rule magic(X):- wizard(X) needed to be moved
 * or removed because wizard/1 is an undefined term. For simplicity, it is
 * commented out. However, another way to fix the problem would be to move the
 * magic(X):- witch(X) rule in front of the one containing wizard/1 before
 * running this query, since it would find its successful match before trying
 * to unify with wizard/1.
 * 
 * Returns true. With the rules for functor magic/1, X is instantiated as
 * 'McGonagall' (a valid atom), which first fails to unify with any fact for
 * house_elf/1, but once it checks the second rule, unifies for witch/1 with the
 * witch('McGonagall') fact.
 */

?- magic(Hermione).
/**
 * Returns the following:
 *  Hermione = dobby ;
 *  Hermione = hermione ;
 *  Hermione = 'McGonagall' ;
 *  Hermione = rita_skeeter.
 * Hermione is a variable (begins with capital letter), so it unifies with the
 * atoms which satisfy the rules for magic/1. The first result it finds is dobby
 * since magic/1 
 */