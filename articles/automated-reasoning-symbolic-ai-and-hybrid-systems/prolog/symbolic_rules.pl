fact(has_documentation).
fact(logs_decisions).

rule(traceable_system) :-
    fact(has_documentation),
    fact(logs_decisions).

% Query example:
% ?- rule(traceable_system).
