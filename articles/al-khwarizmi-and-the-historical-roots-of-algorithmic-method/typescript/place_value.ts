const digits = [1, 2, 3, 0];
const value = digits.reduce((acc, digit) => acc * 10 + digit, 0);
console.log(`place_value_result=${value}`);
