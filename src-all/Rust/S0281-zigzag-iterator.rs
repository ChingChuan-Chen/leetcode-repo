/*
Given two 1d vectors, implement an iterator to return their elements alternately.

 

Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6] 
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].

 

Follow up:
What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question:
The &quot;Zigzag&quot; order is not clearly defined and is ambiguous for k > 2 cases. If &quot;Zigzag&quot; does not look right to you, replace &quot;Zigzag&quot; with &quot;Cyclic&quot;. For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].


*/
pub struct Solution {}
struct ZigzagIterator {
    
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ZigzagIterator {
    /** initialize your data structure here. */
    
    fn new(v1: Vec<i32>, v2: Vec<i32>) -> Self {
        
    }
    
    fn next(&self) -> i32 {
        
    }
    
    fn has_next(&self) -> bool {
        
    }
}

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * let obj = ZigzagIterator::new(v1, v2);
 * let ret_1: i32 = obj.next();
 * let ret_2: bool = obj.has_next();
 */

fn main() {
  assert_eq!(0, Solution::new(0));
  println!("Pass test cases!");
}
