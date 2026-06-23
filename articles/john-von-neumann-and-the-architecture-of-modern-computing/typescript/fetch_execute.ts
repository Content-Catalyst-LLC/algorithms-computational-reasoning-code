type Instruction = { op: string; arg: number };

const program: Instruction[] = [
  { op: "LOAD", arg: 2 },
  { op: "ADD", arg: 3 },
  { op: "STORE", arg: 0 },
  { op: "HALT", arg: 0 },
];

let acc = 0;
for (const inst of program) {
  if (inst.op === "LOAD") acc = inst.arg;
  else if (inst.op === "ADD") acc += inst.arg;
  else if (inst.op === "STORE") console.log(`store address=${inst.arg} value=${acc}`);
  else if (inst.op === "HALT") {
    console.log(`halt accumulator=${acc}`);
    break;
  }
}
