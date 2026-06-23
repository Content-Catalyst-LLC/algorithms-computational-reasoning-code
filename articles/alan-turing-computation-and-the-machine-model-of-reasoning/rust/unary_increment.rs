fn unary_increment(input: &str) -> String {
    let mut tape: Vec<char> = input.chars().collect();
    let mut i = 0;
    while i < tape.len() && tape[i] == '1' {
        i += 1;
    }
    if i == tape.len() {
        tape.push('_');
    }
    tape[i] = '1';
    if i + 1 == tape.len() {
        tape.push('_');
    }
    tape.into_iter().collect()
}

fn main() {
    println!("incremented_tape={}", unary_increment("111_"));
}
