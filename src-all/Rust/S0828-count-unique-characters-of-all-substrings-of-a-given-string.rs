/*
Let&#39;s define a function countUniqueChars(s) that returns the number of unique characters on s, for example if s = &quot;LEETCODE&quot; then &quot;L&quot;, &quot;T&quot;,&quot;C&quot;,&quot;O&quot;,&quot;D&quot; are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.

On this problem given a string s we need to return the sum of countUniqueChars(t) where t is a substring of s. Notice that some substrings can be repeated so on this case you have to count the repeated ones too.

Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.

 
Example 1:
Input: s = &quot;ABC&quot;
Output: 10
Explanation: All possible substrings are: &quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;AB&quot;,&quot;BC&quot; and &quot;ABC&quot;.
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

Example 2:
Input: s = &quot;ABA&quot;
Output: 8
Explanation: The same as example 1, except countUniqueChars(&quot;ABA&quot;) = 1.

Example 3:
Input: s = &quot;LEETCODE&quot;
Output: 92

 
Constraints:
	0 <= s.length <= 10^4
	s contain upper-case English letters only.


*/
pub struct Solution {}
impl Solution {
    pub fn unique_letter_string(s: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::unique_letter_string(0));
  println!("Pass test cases!");
}
