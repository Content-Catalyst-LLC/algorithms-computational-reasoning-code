% Simple scientific computing facts and review rules.
method(finite_difference, derivative_approximation).
method(trapezoid_rule, numerical_integration).
method(runge_kutta, ode_solver).
risk(floating_point_roundoff).
risk(discretization_error).
risk(unstable_step_size).
requires_review(Method) :- method(Method, _).
