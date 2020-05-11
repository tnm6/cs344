/**
 * Exercise 13.1 for CS-344, Professor Keith VanderLinden, Calvin University
 * Answers by Nathan Meyer (tnm6)
 */

% a. Exercises from LPN!
%   i.  Exercise 3.2
directlyIn(natasha, irina).
directlyIn(olga, natasha).
directlyIn(katarina, olga).

in(X, Y):- directlyIn(X, Y).

in(X, Y):- directlyIn(X, Z),
              in(Z, Y).

?- in(katarina,natasha).
% resolves to true
?- in(olga,katarina).
% resolves to false

%   ii. Exercise 4.5
tran(eins, one). 
tran(zwei, two). 
tran(drei, three). 
tran(vier, four). 
tran(fuenf, five). 
tran(sechs, six). 
tran(sieben, seven). 
tran(acht, eight). 
tran(neun, nine).

listtran([], []).
listtran([X|Tx], [Y|Ty]):- tran(X, Y),
                              listtran(Tx, Ty).

?- listtran([eins,neun,zwei],X).
% resolves to X = [one, nine, two].
?- listtran(X,[one,seven,six,two]).
% resolves to X = [eins, sieben, sechs, zwei].


% b. Does Prolog implement a version of generalized modus ponens?
% Yes, it does. Given this simple knowledge base:
flies(X):- plane(X).
plane(747).
% where plane(X) implies flies(X), and plane(747) is true, so
?- flies(747).
% also returns true. And
?- flies(X).
% returns 747, using the variable X and instantiating it to the first (and only)
% result which satisfies the rule plane(X), X = 747.