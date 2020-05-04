/**
 * Exercise 12.1 for CS-344, Professor Keith VanderLinden, Calvin University
 * Answers by Nathan Meyer (tnm6)
 */

% a. From LPN!
%   i. Exercise 1.4
killer(butch).
married(mia, marsellus).
dead(zed).
kills(marsellus,X):-footmassage(X,mia).
loves(mia, X):-goodDancer(X).
eats(jules, X):-nutritious(X); tasty(X).
/**
 * 1.–3. are simple facts of arity 1 or 2, so they are written as such.
 * 4.–6. are conditional rules, so they are written as such, and the variable X
 *   is used to account for "everyone/anyone/anything" in the prompts.
 */

%   i. Exercise 1.5
wizard(ron).
% yes, because it is a stated fact in the knowledge base
witch(ron).
% no, because no fact or rule in the knowledge base defines predicate witch
wizard(hermione).
% no, because hermione is not found in the knowledge base
witch(hermione).
% no, both witch and hermione are not found in knowledge base
wizard(harry).
% yes, because harry has a wand and is a quidditch player, so he has a broom, so
%   both conditions for wizard(X) rule are fulfilled
wizard(Y).
% ron, becuase ron is the first to be defined in wizard fact in knowledge base
witch(Y).
% no (or error), because no witch facts have been defined in knowledge base

% b. Modus ponens and Prolog
/**
 * Yes, Prolog does implement the deduction step of modus ponens. As
 * demonstrated in the chapter (section 1.1), the following knowledge base is
 * used as an example:
 */
happy(yolanda). 
listens2Music(mia). 
listens2Music(yolanda):- happy(yolanda). 
playsAirGuitar(mia):- listens2Music(mia). 
playsAirGuitar(yolanda):- listens2Music(yolanda).

?- playsAirGuitar(mia).
/**
 * Since Prolog implements modus ponens, this query will return yes, since even
 * though it is not explicitly defined, it can be deduced since
 * listen2Music(mia) is defined as a fact and the rule
 * playsAirGuitar(mia):- listens2Music(mia) is also defined.
 */

% c. Compare and contrast Horn clauses and propositional logic.
/**
 * Horn clauses have their power in representing complete ideas of predicates
 * and their subjects, like happy(yolanda) and listens2Music:- happy(mia),
 * whereas in propositional logic, these would have to be two separate labels
 * like Y and M with no explicit relation between the two. However,
 * propositional logic, in strictly terms of evaluating propositions as true or
 * false, is more succinct, as Y ^ M is more concise than happy(yolanda),
 * happy(mia).
 */

% d. Does Prolog distinguish TELL and ASK?
/**
 * Yes. Facts like wizard(harry) TELL the knowledge base agent information, and
 * queries like ?- happy(yolanda) and ?- happy(X) ASK the knowledge base to
 * perform an action on the knowledge it has been told.
 */