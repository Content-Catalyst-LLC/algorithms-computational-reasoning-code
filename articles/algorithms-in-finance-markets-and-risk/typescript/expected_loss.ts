const pd = 0.035;
const lgd = 0.45;
const ead = 100000.0;
const expectedLoss = pd * lgd * ead;
console.log(`expected_loss=${expectedLoss.toFixed(4)}`);
