/*
You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.

You are also given an integer maxCost.

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of twith a cost less than or equal to maxCost.

If there is no substring from s that can be changed to its corresponding substring from t, return 0.

 
Example 1:
Input: s = &quot;abcd&quot;, t = &quot;bcdf&quot;, maxCost = 3
Output: 3
Explanation: &quot;abc&quot; of s can change to &quot;bcd&quot;. That costs 3, so the maximum length is 3.

Example 2:
Input: s = &quot;abcd&quot;, t = &quot;cdef&quot;, maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to charactor in t, so the maximum length is 1.

Example 3:
Input: s = &quot;abcd&quot;, t = &quot;acde&quot;, maxCost = 0
Output: 1
Explanation: You can&#39;t make any change, so the maximum length is 1.

 
Constraints:
	1 <= s.length, t.length <= 10^5
	0 <= maxCost <= 10^6
	s and t only contain lower case English letters.


*/
pub struct Solution {}
impl Solution {
    pub fn equal_substring(s: String, t: String, max_cost: i32) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::equal_substring(0));
  println!("Pass test cases!");
}
