const probability = 0.82;
const benefitIfAct = 0.88;
const costIfAct = 0.30;
const expectedValue = probability * benefitIfAct - costIfAct;
console.log(`expected_value_of_action=${expectedValue.toFixed(4)}`);
