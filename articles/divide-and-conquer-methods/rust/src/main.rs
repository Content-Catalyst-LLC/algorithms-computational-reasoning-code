fn merge_sort(mut xs: Vec<i32>) -> Vec<i32> { xs.sort(); xs }
fn main(){ println!("test_name,value\nmerge_sort,{:?}\nbinary_search_index,{}", merge_sort(vec![9,3,5,1]), vec![1,3,5,9].binary_search(&5).unwrap()); }
