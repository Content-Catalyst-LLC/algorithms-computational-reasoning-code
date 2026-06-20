#[derive(Clone)]
struct Alternative { name: &'static str, cost: f64, risk: f64, quality: f64 }

fn min_max(xs: &[f64]) -> (f64, f64) {
    xs.iter().fold((xs[0], xs[0]), |(mn, mx), &x| (mn.min(x), mx.max(x)))
}
fn norm_min(x: f64, xs: &[f64]) -> f64 { let (mn, mx) = min_max(xs); if mx == mn { 1.0 } else { (mx - x) / (mx - mn) } }
fn norm_max(x: f64, xs: &[f64]) -> f64 { let (mn, mx) = min_max(xs); if mx == mn { 1.0 } else { (x - mn) / (mx - mn) } }

fn main() {
    let alts = vec![
        Alternative { name: "A", cost: 72.0, risk: 34.0, quality: 82.0 },
        Alternative { name: "B", cost: 64.0, risk: 41.0, quality: 76.0 },
        Alternative { name: "C", cost: 81.0, risk: 26.0, quality: 88.0 },
        Alternative { name: "D", cost: 58.0, risk: 52.0, quality: 69.0 },
    ];
    let costs = [72.0, 64.0, 81.0, 58.0]; let risks = [34.0, 41.0, 26.0, 52.0]; let qualities = [82.0, 76.0, 88.0, 69.0];
    for a in alts { println!("{} {:.6}", a.name, 0.35*norm_min(a.cost,&costs)+0.30*norm_min(a.risk,&risks)+0.35*norm_max(a.quality,&qualities)); }
}
