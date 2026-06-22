program stock_flow_update
  implicit none
  real :: current_stock, inflow, outflow, next_stock
  current_stock = 100.0
  inflow = 12.0
  outflow = 7.0
  next_stock = current_stock + inflow - outflow
  print *, "next_stock=", next_stock
end program stock_flow_update
