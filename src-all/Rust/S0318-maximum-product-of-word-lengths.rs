/*
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Input: [&quot;abcw&quot;,&quot;baz&quot;,&quot;foo&quot;,&quot;bar&quot;,&quot;xtfn&quot;,&quot;abcdef&quot;]
Output: 16 
Explanation: The two words can be &quot;abcw&quot;, &quot;xtfn&quot;.

Example 2:
Input: [&quot;a&quot;,&quot;ab&quot;,&quot;abc&quot;,&quot;d&quot;,&quot;cd&quot;,&quot;bcd&quot;,&quot;abcd&quot;]
Output: 4 
Explanation: The two words can be &quot;ab&quot;, &quot;cd&quot;.

Example 3:
Input: [&quot;a&quot;,&quot;aa&quot;,&quot;aaa&quot;,&quot;aaaa&quot;]
Output: 0 
Explanation: No such pair of words.

 
Constraints:
	0 <= words.length <= 10^3
	0 <= words[i].length <= 10^3
	words[i] consists only of lowercase English letters.


*/
pub struct Solution {}
impl Solution {
    pub fn max_product(words: Vec<String>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::max_product(0));
  println!("Pass test cases!");
}
