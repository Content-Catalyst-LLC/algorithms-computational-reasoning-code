public class FetchExecute {
    static class Instruction {
        String op;
        int arg;
        Instruction(String op, int arg) { this.op = op; this.arg = arg; }
    }

    public static void main(String[] args) {
        Instruction[] program = {
            new Instruction("LOAD", 2),
            new Instruction("ADD", 3),
            new Instruction("STORE", 0),
            new Instruction("HALT", 0)
        };
        int acc = 0;
        for (Instruction inst : program) {
            switch (inst.op) {
                case "LOAD": acc = inst.arg; break;
                case "ADD": acc += inst.arg; break;
                case "STORE": System.out.printf("store address=%d value=%d%n", inst.arg, acc); break;
                case "HALT": System.out.printf("halt accumulator=%d%n", acc); return;
            }
        }
    }
}
