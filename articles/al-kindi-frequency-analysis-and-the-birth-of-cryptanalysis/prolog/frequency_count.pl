% Simple illustrative fact pattern for toy frequency reasoning.
count_symbol(Symbol, Text, Count) :-
    include(=(Symbol), Text, Matches),
    length(Matches, Count).

% Query example:
% ?- count_symbol(a, [a,b,a,c], Count).
