/*
Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string &quot;&quot;.

Example 1:
Input: s = &quot;aabbcc&quot;, k = 3
Output: &quot;abcabc&quot; 
Explanation: The same letters are at least distance 3 from each other.

Example 2:
Input: s = &quot;aaabc&quot;, k = 3
Output: &quot;&quot; 
Explanation: It is not possible to rearrange the string.

Example 3:
Input: s = &quot;aaadbbcc&quot;, k = 2
Output: &quot;abacabcd&quot;
Explanation: The same letters are at least distance 2 from each other.


*/
pub struct Solution {}
impl Solution {
    pub fn rearrange_string(s: String, k: i32) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::rearrange_string(0));
  println!("Pass test cases!");
}
