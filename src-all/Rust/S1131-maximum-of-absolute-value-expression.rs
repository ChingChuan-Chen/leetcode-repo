/*
Given two arrays of integers with equal lengths, return the maximum value of:

|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

where the maximum is taken over all 0 <= i, j < arr1.length.

 
Example 1:
Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13

Example 2:
Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
Output: 20

 
Constraints:
	2 <= arr1.length == arr2.length <= 40000
	-10^6 <= arr1[i], arr2[i] <= 10^6


*/
pub struct Solution {}
impl Solution {
    pub fn max_abs_val_expr(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::max_abs_val_expr(0));
  println!("Pass test cases!");
}
