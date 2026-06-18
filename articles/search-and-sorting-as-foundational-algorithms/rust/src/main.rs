fn linear_search(values: &[i32], target: i32) -> isize {
    values.iter().position(|x| *x == target).map(|i| i as isize).unwrap_or(-1)
}
fn main(){ let mut xs=vec![7,2,9,1]; xs.sort(); println!("test_name,value\nlinear_search_9,{}\nsort_demo,{:?}", linear_search(&[7,2,9,1],9), xs); }
