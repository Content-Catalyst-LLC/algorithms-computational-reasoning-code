share(Total, Weight, WeightSum, Share) :-
    Share is Total * Weight / WeightSum.

% Query example:
% ?- share(1200, 2, 4, Share).
