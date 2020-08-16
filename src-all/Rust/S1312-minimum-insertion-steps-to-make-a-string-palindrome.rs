/*
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 
Example 1:
Input: s = &quot;zzazz&quot;
Output: 0
Explanation: The string &quot;zzazz&quot; is already palindrome we don&#39;t need any insertions.

Example 2:
Input: s = &quot;mbadm&quot;
Output: 2
Explanation: String can be &quot;mbdadbm&quot; or &quot;mdbabdm&quot;.

Example 3:
Input: s = &quot;leetcode&quot;
Output: 5
Explanation: Inserting 5 characters the string becomes &quot;leetcodocteel&quot;.

Example 4:
Input: s = &quot;g&quot;
Output: 0

Example 5:
Input: s = &quot;no&quot;
Output: 1

 
Constraints:
	1 <= s.length <= 500
	All characters of s are lower case English letters.

*/
pub struct Solution {}
impl Solution {
    pub fn min_insertions(s: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::min_insertions(0));
  println!("Pass test cases!");
}
