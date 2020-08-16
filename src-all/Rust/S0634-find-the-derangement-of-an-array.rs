/*

In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position.

There's originally an array consisting of n integers from 1 to n in ascending order, you need to find the number of derangement it can generate.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: 3
Output: 2
Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] and [3,1,2].

Note:
n is in the range of [1, 106].

*/
pub struct Solution {}
impl Solution {
    pub fn find_derangement(n: i32) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::find_derangement(0));
  println!("Pass test cases!");
}
