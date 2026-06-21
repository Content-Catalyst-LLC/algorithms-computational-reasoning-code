function f(x: number): number { return Math.sin(x) + 0.25 * x * x; }
function centralDifference(x: number, h: number): number { return (f(x + h) - f(x - h)) / (2 * h); }
console.log(centralDifference(1.0, 0.01).toFixed(12));
