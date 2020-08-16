/*
Given an array of string words. Return all strings in words which is substring of another word in any order. 

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

 
Example 1:
Input: words = [&quot;mass&quot;,&quot;as&quot;,&quot;hero&quot;,&quot;superhero&quot;]
Output: [&quot;as&quot;,&quot;hero&quot;]
Explanation: &quot;as&quot; is substring of &quot;mass&quot; and &quot;hero&quot; is substring of &quot;superhero&quot;.
[&quot;hero&quot;,&quot;as&quot;] is also a valid answer.

Example 2:
Input: words = [&quot;leetcode&quot;,&quot;et&quot;,&quot;code&quot;]
Output: [&quot;et&quot;,&quot;code&quot;]
Explanation: &quot;et&quot;, &quot;code&quot; are substring of &quot;leetcode&quot;.

Example 3:
Input: words = [&quot;blue&quot;,&quot;green&quot;,&quot;bu&quot;]
Output: []

 
Constraints:
	1 <= words.length <= 100
	1 <= words[i].length <= 30
	words[i] contains only lowercase English letters.
	It&#39;s guaranteed that words[i] will be unique.

*/
pub struct Solution {}
impl Solution {
    pub fn string_matching(words: Vec<String>) -> Vec<String> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::string_matching(0));
  println!("Pass test cases!");
}
