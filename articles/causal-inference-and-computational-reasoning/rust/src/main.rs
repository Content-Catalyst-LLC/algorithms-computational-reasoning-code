#[derive(Debug)]
struct Contrast {
    treated_mean: f64,
    control_mean: f64,
}

impl Contrast {
    fn effect(&self) -> f64 {
        self.treated_mean - self.control_mean
    }
}

fn main() {
    let contrast = Contrast { treated_mean: 0.64, control_mean: 0.47 };
    println!("causal contrast = {:.4}", contrast.effect());
}
