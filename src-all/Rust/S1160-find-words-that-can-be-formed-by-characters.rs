/*
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:
Input: words = [&quot;cat&quot;,&quot;bt&quot;,&quot;hat&quot;,&quot;tree&quot;], chars = &quot;atach&quot;
Output: 6
Explanation: 
The strings that can be formed are &quot;cat&quot; and &quot;hat&quot; so the answer is 3 + 3 = 6.

Example 2:
Input: words = [&quot;hello&quot;,&quot;world&quot;,&quot;leetcode&quot;], chars = &quot;welldonehoneyr&quot;
Output: 10
Explanation: 
The strings that can be formed are &quot;hello&quot; and &quot;world&quot; so the answer is 5 + 5 = 10.

 

Note:
	1 <= words.length <= 1000
	1 <= words[i].length, chars.length <= 100
	All strings contain lowercase English letters only.

*/
pub struct Solution {}
impl Solution {
    pub fn count_characters(words: Vec<String>, chars: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::count_characters(0));
  println!("Pass test cases!");
}
