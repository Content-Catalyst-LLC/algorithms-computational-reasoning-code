fn church_apply<F>(n: usize, mut f: F, mut x: i32) -> i32
where
    F: FnMut(i32) -> i32,
{
    for _ in 0..n {
        x = f(x);
    }
    x
}

fn main() {
    println!("church_3_successor_0={}", church_apply(3, |x| x + 1, 0));
}
