fn schema_quality(fields:f64, keys:f64, constraints:f64, metadata:f64, lineage:f64) -> f64 {
    100.0 * (0.22*fields + 0.20*keys + 0.20*constraints + 0.20*metadata + 0.18*lineage)
}
fn main(){ println!("test_name,value\nschema_quality_score,{:.3}", schema_quality(0.90,0.85,0.80,0.88,0.82)); }
