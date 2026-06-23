fn main() {
    let program = [("LOAD", 2), ("ADD", 3), ("STORE", 0), ("HALT", 0)];
    let mut acc = 0;
    for (op, arg) in program {
        match op {
            "LOAD" => acc = arg,
            "ADD" => acc += arg,
            "STORE" => println!("store address={} value={}", arg, acc),
            "HALT" => {
                println!("halt accumulator={}", acc);
                break;
            }
            _ => {}
        }
    }
}
