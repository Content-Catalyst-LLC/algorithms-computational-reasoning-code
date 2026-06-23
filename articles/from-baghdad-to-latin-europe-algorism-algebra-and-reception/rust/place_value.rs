fn main() {
    let digits = [1, 2, 3, 0];
    let value = digits.iter().fold(0, |acc, digit| acc * 10 + digit);
    println!("place_value={}", value);
}
