/*
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

 
Example 1:
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

 
Constraints:
	0 <= nums.length <= 10^5
	-10^4 <= nums[i] <= 10^4


*/
pub struct Solution {}
impl Solution {
    pub fn count_smaller(nums: Vec<i32>) -> Vec<i32> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::count_smaller(0));
  println!("Pass test cases!");
}
