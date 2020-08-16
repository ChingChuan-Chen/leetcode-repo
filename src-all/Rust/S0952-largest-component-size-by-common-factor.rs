/*
Given a non-empty array of unique positive integers A, consider the following graph:

	There are A.length nodes, labelled A[0] to A[A.length - 1];
	There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.

Return the size of the largest connected component in the graph.

 

Example 1:
Input: [4,6,15,35]
Output: 4

Example 2:
Input: [20,50,9,63]
Output: 2

Example 3:
Input: [2,3,6,7,4,12,21,39]
Output: 8

Note:
	1 <= A.length <= 20000
	1 <= A[i] <= 100000


*/
pub struct Solution {}
impl Solution {
    pub fn largest_component_size(a: Vec<i32>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::largest_component_size(0));
  println!("Pass test cases!");
}
