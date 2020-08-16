/*
Given a string num representing the digits of a very large integer and an integer k.

You are allowed to swap any two adjacent digits of the integer at most k times.

Return the minimum integer you can obtain also as a string.

 
Example 1:
Input: num = &quot;4321&quot;, k = 4
Output: &quot;1342&quot;
Explanation: The steps to obtain the minimum integer from 4321 with 4 adjacent swaps are shown.

Example 2:
Input: num = &quot;100&quot;, k = 1
Output: &quot;010&quot;
Explanation: It&#39;s ok for the output to have leading zeros, but the input is guaranteed not to have any leading zeros.

Example 3:
Input: num = &quot;36789&quot;, k = 1000
Output: &quot;36789&quot;
Explanation: We can keep the number without any swaps.

Example 4:
Input: num = &quot;22&quot;, k = 22
Output: &quot;22&quot;

Example 5:
Input: num = &quot;9438957234785635408&quot;, k = 23
Output: &quot;0345989723478563548&quot;

 
Constraints:
	1 <= num.length <= 30000
	num contains digits only and doesn&#39;t have leading zeros.
	1 <= k <= 10^9


*/
pub struct Solution {}
impl Solution {
    pub fn min_integer(num: String, k: i32) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::min_integer(0));
  println!("Pass test cases!");
}
