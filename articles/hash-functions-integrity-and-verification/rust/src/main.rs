fn teaching_checksum(s: &str) -> u64 {
    s.bytes()
        .enumerate()
        .map(|(i, b)| (i as u64 + 1) * b as u64)
        .sum::<u64>()
        % 1_000_003
}

fn main() {
    let original = "verified artifact manifest";
    let altered = "verified artifact manifest!";
    println!("original checksum={}", teaching_checksum(original));
    println!("altered checksum={}", teaching_checksum(altered));
    println!("match={}", teaching_checksum(original) == teaching_checksum(altered));
}
