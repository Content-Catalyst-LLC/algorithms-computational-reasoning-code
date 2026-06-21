program model_validation_metrics
  implicit none
  real :: observed(5) = (/33.1, 39.7, 38.8, 39.3, 8.4/)
  real :: predicted(5) = (/31.92, 31.58, 36.48, 25.30, 11.30/)
  real :: err(5), rmse, mae
  err = observed - predicted
  rmse = sqrt(sum(err * err) / 5.0)
  mae = sum(abs(err)) / 5.0
  print *, 'rmse=', rmse
  print *, 'mae=', mae
end program model_validation_metrics
