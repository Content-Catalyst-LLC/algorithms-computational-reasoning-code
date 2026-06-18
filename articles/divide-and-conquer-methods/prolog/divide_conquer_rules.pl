divide_conquer_step(divide).
divide_conquer_step(solve).
divide_conquer_step(combine).
base_case(size_zero_or_one).
progress_measure(subproblem_size_decreases).
recurrence(merge_sort, 'T(n)=2T(n/2)+O(n)').
recurrence(binary_search, 'T(n)=T(n/2)+O(1)').
