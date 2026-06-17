automated_reasoning_quality('SAT solver workflow', 80.44).
automated_reasoning_quality('Model checking workflow', 81.76).
automated_reasoning_quality('Institutional rule engine', 78.80).
automated_reasoning_quality('AI-assisted theorem proving', 80.64).

premise(human_socrates).
rule(mortal_if_human).
conclusion(mortal_socrates) :- premise(human_socrates), rule(mortal_if_human).
