fn binary_fitness(candidate: &[i32]) -> i32 { candidate.iter().sum() }
fn main(){ println!("test_name,value\nbinary_fitness,{}\nmutation_rate,0.03", binary_fitness(&[1,0,1,1])); }
