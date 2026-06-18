fn speedup(t1:f64,tp:f64)->f64{ if tp==0.0 {0.0} else {t1/tp} }
fn amdahl(p:f64,s:f64)->f64{ if p==0.0 {0.0} else {1.0/(s+((1.0-s)/p))} }
fn efficiency(p:f64,sp:f64)->f64{ if p==0.0 {0.0} else {sp/p} }
fn main(){ let sp=speedup(120.0,28.0); println!("test_name,value\nobserved_speedup_120_to_28,{:.4}\namdahl_speedup_8_workers,{:.4}\nefficiency_8_workers,{:.4}", sp, amdahl(8.0,0.12), efficiency(8.0,sp)); }
