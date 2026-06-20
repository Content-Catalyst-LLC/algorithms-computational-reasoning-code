fn feasible(x: i32, y: i32) -> bool {
    2 * x + y <= 8 && x + 2 * y <= 8 && x >= 0 && y >= 0
}

fn objective(x: i32, y: i32) -> i32 {
    3 * x + 4 * y
}

fn main() {
    let mut best = (0, 0, i32::MIN);
    for x in 0..10 {
        for y in 0..10 {
            if feasible(x, y) {
                let value = objective(x, y);
                if value > best.2 {
                    best = (x, y, value);
                }
            }
        }
    }
    println!("best x={} y={} objective={}", best.0, best.1, best.2);
}
