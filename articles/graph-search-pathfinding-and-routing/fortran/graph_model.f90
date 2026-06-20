program graph_model
  real :: density
  density = 7.0 / (5.0 * 4.0)
  print '(A)', 'test_name value'
  print '(A,I10)', 'node_count ', 5
  print '(A,I10)', 'edge_count ', 7
  print '(A,F10.6)', 'density ', density
  print '(A,F10.3)', 'manual_shortest_path_cost ', 5.5
end program graph_model
