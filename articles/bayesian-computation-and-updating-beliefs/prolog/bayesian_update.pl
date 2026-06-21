:- initialization(main).
main :- PostAlpha is 2.0 + 113.0, PostBeta is 2.0 + 72.0, Mean is PostAlpha / (PostAlpha + PostBeta), format('posterior_mean=~6f~n', [Mean]), halt.
