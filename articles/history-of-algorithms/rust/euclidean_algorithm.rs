fn gcd_algorithm(mut a: i64, mut b: i64) -> i64 {
    while b != 0 {
        let r = a % b;
        a = b;
        b = r;
    }
    a.abs()
}

fn main() {
    println!("gcd={}", gcd_algorithm(252, 105));
}
