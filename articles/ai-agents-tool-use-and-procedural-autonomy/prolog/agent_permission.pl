tool_risk(email_send, 0.85).
approval_required(email_send).
not_approved(email_send).

status(Tool, blocked) :-
    approval_required(Tool),
    not_approved(Tool).

status(Tool, escalate) :-
    tool_risk(Tool, Risk),
    Risk >= 0.65.

% Query example:
% ?- status(email_send, Status).
