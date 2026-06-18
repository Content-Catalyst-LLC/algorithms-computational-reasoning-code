fn query_logic_score(entity:f64, relationship:f64, predicate:f64, join:f64, keys:f64, missingness:f64) -> f64 {
    100.0 * (0.18*entity + 0.18*relationship + 0.18*predicate + 0.18*join + 0.14*keys + 0.14*missingness)
}
fn main(){ println!("test_name,value\nquery_logic_core_score,{:.3}", query_logic_score(.88,.86,.84,.82,.84,.80)); }
