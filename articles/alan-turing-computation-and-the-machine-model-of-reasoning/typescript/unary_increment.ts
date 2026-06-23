function unaryIncrement(input: string): string {
  const tape = input.split("");
  let i = 0;
  while (i < tape.length && tape[i] === "1") {
    i += 1;
  }
  if (i === tape.length) {
    tape.push("_");
  }
  tape[i] = "1";
  if (i + 1 === tape.length) {
    tape.push("_");
  }
  return tape.join("");
}

console.log(`incremented_tape=${unaryIncrement("111_")}`);
