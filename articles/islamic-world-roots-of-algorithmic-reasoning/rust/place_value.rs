fn main() {
    let digit: i32 = 7;
    let base: i32 = 10;
    let position: u32 = 3;
    let value = digit * base.pow(position);
    println!("place_value={}", value);
}
