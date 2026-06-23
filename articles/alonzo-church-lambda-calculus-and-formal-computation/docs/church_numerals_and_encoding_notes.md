# Church Numerals and Encoding Notes

Church numerals encode natural numbers as repeated function application:

- 0 = λf. λx. x
- 1 = λf. λx. f x
- 2 = λf. λx. f (f x)
- n = λf. λx. f^n(x)

This shows that data can be represented within a formal calculus. Numbers, booleans, pairs, and lists can be encoded as functions.
