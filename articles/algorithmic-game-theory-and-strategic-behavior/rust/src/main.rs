fn main() {
    let profiles = [("cooperate", "cooperate", 3.0, 3.0), ("cooperate", "defect", 0.0, 5.0), ("defect", "cooperate", 5.0, 0.0), ("defect", "defect", 1.0, 1.0)];
    for (p1, p2, u1, u2) in profiles { println!("{p1}/{p2}: welfare={}", u1 + u2); }
}
