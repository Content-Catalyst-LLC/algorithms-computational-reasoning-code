stock_flow_update(CurrentStock, Inflow, Outflow, NextStock) :-
    NextStock is CurrentStock + Inflow - Outflow.

% Query example:
% ?- stock_flow_update(100, 12, 7, NextStock).
