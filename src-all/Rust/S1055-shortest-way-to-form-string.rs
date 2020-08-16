/*
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 

Example 1:
Input: source = &quot;abc&quot;, target = &quot;abcbc&quot;
Output: 2
Explanation: The target &quot;abcbc&quot; can be formed by &quot;abc&quot; and &quot;bc&quot;, which are subsequences of source &quot;abc&quot;.

Example 2:
Input: source = &quot;abc&quot;, target = &quot;acdbc&quot;
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character &quot;d&quot; in target string.

Example 3:
Input: source = &quot;xyz&quot;, target = &quot;xzyxz&quot;
Output: 3
Explanation: The target string can be constructed as follows &quot;xz&quot; + &quot;y&quot; + &quot;xz&quot;.

 
Constraints:
	Both the source and target strings consist of only lowercase English letters from &quot;a&quot;-&quot;z&quot;.
	The lengths of source and target string are between 1 and 1000.

*/
pub struct Solution {}
impl Solution {
    pub fn shortest_way(source: String, target: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::shortest_way(0));
  println!("Pass test cases!");
}
