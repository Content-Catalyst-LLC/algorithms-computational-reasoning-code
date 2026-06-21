artifact(code).
artifact(data).
artifact(parameters).
artifact(environment).
artifact(outputs).
artifact(logs).
artifact(validation).

review_complete :-
  artifact(code), artifact(data), artifact(parameters), artifact(environment), artifact(outputs), artifact(logs), artifact(validation).
