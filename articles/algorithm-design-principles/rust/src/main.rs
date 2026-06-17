fn nondecreasing(values: &[i32]) -> bool { values.windows(2).all(|w| w[0] <= w[1]) }
fn main(){ println!("test_name,status"); println!("sorted_valid,{}", if nondecreasing(&[1,2,2,3]) {"pass"} else {"fail"}); println!("sorted_invalid,{}", if nondecreasing(&[1,3,2]) {"pass"} else {"fail"}); }
