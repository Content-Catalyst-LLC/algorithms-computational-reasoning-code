representation_quality('Institutional archive records', 88.92).
representation_quality('Web media delivery', 84.32).
representation_quality('Scientific simulation outputs', 87.08).
representation_quality('AI context packing', 81.22).

requires_lossless('Institutional archive records').
requires_lossless('Scientific simulation outputs').
preserve_metadata(X) :- representation_quality(X, _).
