tree_structure_quality('Document outline tree', 81.40).
tree_structure_quality('Syntax tree', 85.56).
tree_structure_quality('Decision classification tree', 82.00).
tree_structure_quality('Database B-tree index', 84.32).

child(root, left).
child(root, right).
child(left, left_leaf).
child(right, right_a).
child(right, right_b).

ancestor(X, Y) :- child(X, Y).
ancestor(X, Y) :- child(X, Z), ancestor(Z, Y).
