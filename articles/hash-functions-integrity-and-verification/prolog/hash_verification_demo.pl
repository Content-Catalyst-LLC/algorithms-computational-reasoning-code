% Hash verification teaching checksum in Prolog.
checksum(Text, Sum) :-
    string_codes(Text, Codes),
    checksum_codes(Codes, 1, 0, Sum).

checksum_codes([], _, Acc, Sum) :- Sum is Acc mod 1000003.
checksum_codes([C|Rest], I, Acc, Sum) :-
    Acc1 is Acc + C * I,
    I1 is I + 1,
    checksum_codes(Rest, I1, Acc1, Sum).

:- initialization(main).
main :-
    checksum("verified artifact manifest", A),
    checksum("verified artifact manifest!", B),
    format('original checksum=~w~n', [A]),
    format('altered checksum=~w~n', [B]),
    format('match=~w~n', [A =:= B]),
    halt.
