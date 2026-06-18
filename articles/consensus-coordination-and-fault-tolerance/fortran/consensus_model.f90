program consensus_model
  print '(A)', 'test_name value'
  print '(A,I5)', 'majority_quorum_5_nodes ', 5 / 2 + 1
  print '(A,I5)', 'crash_fault_tolerance_5_nodes ', (5 - 1) / 2
  print '(A,I5)', 'byzantine_replicas_for_2_faults ', 3 * 2 + 1
end program consensus_model
