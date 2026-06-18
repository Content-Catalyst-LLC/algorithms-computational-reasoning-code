use std::collections::HashMap;
fn verify_coloring(edges:&[(u32,u32)], colors:&HashMap<u32,u32>) -> bool {
    edges.iter().all(|(u,v)| colors.get(u) != colors.get(v))
}
fn main(){
    let mut c=HashMap::new(); c.insert(1,1); c.insert(2,2); c.insert(3,1);
    println!("test_name,value\ncoloring_valid,{}", verify_coloring(&[(1,2),(2,3)], &c));
}
