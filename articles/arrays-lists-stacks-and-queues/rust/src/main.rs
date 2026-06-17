use std::collections::VecDeque;

fn main() {
    let mut stack = vec!["first", "second", "third"];
    let mut queue: VecDeque<&str> = VecDeque::from(vec!["first", "second", "third"]);
    println!("case_name,sequence_structure_quality");
    println!("Numerical time series array,83.20");
    println!("Undo action stack,83.80");
    println!("Case review queue,85.04");
    println!("Streaming circular buffer,83.80");
    println!("stack_first_removed,{}", stack.pop().unwrap());
    println!("queue_first_removed,{}", queue.pop_front().unwrap());
}
