/*

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number. 

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.


*/
pub struct Solution {}
impl Solution {
    pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::find_error_nums(0));
  println!("Pass test cases!");
}
