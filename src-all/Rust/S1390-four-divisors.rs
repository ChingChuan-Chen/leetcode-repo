/*
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.

If there is no such integer in the array, return 0.

 
Example 1:
Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.

 
Constraints:
	1 <= nums.length <= 10^4
	1 <= nums[i] <= 10^5


*/
pub struct Solution {}
impl Solution {
    pub fn sum_four_divisors(nums: Vec<i32>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::sum_four_divisors(0));
  println!("Pass test cases!");
}
