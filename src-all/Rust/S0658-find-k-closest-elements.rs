/*
Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

 
Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

 
Constraints:
	1 <= k <= arr.length
	1 <= arr.length <= 10^4
	Absolute value of elements in the array and x will not exceed 104


*/
pub struct Solution {}
impl Solution {
    pub fn find_closest_elements(arr: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::find_closest_elements(0));
  println!("Pass test cases!");
}
