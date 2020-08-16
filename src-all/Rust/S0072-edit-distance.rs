/*
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

	Insert a character
	Delete a character
	Replace a character

Example 1:
Input: word1 = &quot;horse&quot;, word2 = &quot;ros&quot;
Output: 3
Explanation: 
horse -> rorse (replace &#39;h&#39; with &#39;r&#39;)
rorse -> rose (remove &#39;r&#39;)
rose -> ros (remove &#39;e&#39;)

Example 2:
Input: word1 = &quot;intention&quot;, word2 = &quot;execution&quot;
Output: 5
Explanation: 
intention -> inention (remove &#39;t&#39;)
inention -> enention (replace &#39;i&#39; with &#39;e&#39;)
enention -> exention (replace &#39;n&#39; with &#39;x&#39;)
exention -> exection (replace &#39;n&#39; with &#39;c&#39;)
exection -> execution (insert &#39;u&#39;)


*/
pub struct Solution {}
impl Solution {
    pub fn min_distance(word1: String, word2: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::min_distance(0));
  println!("Pass test cases!");
}
