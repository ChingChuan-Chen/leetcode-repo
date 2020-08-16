/*
You are given a string s, a split is called good if you can split s into 2 non-empty strings p and q where its concatenation is equal to s and the number of distinct letters in p and q are the same.

Return the number of good splits you can make in s.

 
Example 1:
Input: s = &quot;aacaba&quot;
Output: 2
Explanation: There are 5 ways to split &quot;aacaba&quot; and 2 of them are good. 
(&quot;a&quot;, &quot;acaba&quot;) Left string and right string contains 1 and 3 different letters respectively.
(&quot;aa&quot;, &quot;caba&quot;) Left string and right string contains 1 and 3 different letters respectively.
(&quot;aac&quot;, &quot;aba&quot;) Left string and right string contains 2 and 2 different letters respectively (good split).
(&quot;aaca&quot;, &quot;ba&quot;) Left string and right string contains 2 and 2 different letters respectively (good split).
(&quot;aacab&quot;, &quot;a&quot;) Left string and right string contains 3 and 1 different letters respectively.

Example 2:
Input: s = &quot;abcd&quot;
Output: 1
Explanation: Split the string as follows (&quot;ab&quot;, &quot;cd&quot;).

Example 3:
Input: s = &quot;aaaaa&quot;
Output: 4
Explanation: All possible splits are good.

Example 4:
Input: s = &quot;acbadbaada&quot;
Output: 2

 
Constraints:
	s contains only lowercase English letters.
	1 <= s.length <= 10^5

*/
pub struct Solution {}
impl Solution {
    pub fn num_splits(s: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::num_splits(0));
  println!("Pass test cases!");
}
