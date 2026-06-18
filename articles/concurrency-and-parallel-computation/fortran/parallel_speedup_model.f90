program parallel_speedup_model
  real :: observed_speedup, amdahl_speedup, efficiency
  observed_speedup = 120.0 / 28.0
  amdahl_speedup = 1.0 / (0.12 + ((1.0 - 0.12) / 8.0))
  efficiency = observed_speedup / 8.0
  print '(A)', 'test_name value'
  print '(A,F10.6)', 'observed_speedup_120_to_28 ', observed_speedup
  print '(A,F10.6)', 'amdahl_speedup_8_workers ', amdahl_speedup
  print '(A,F10.6)', 'efficiency_8_workers ', efficiency
end program parallel_speedup_model
