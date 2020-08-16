/*
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Input: [&quot;abcd&quot;,&quot;dcba&quot;,&quot;lls&quot;,&quot;s&quot;,&quot;sssll&quot;]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are [&quot;dcbaabcd&quot;,&quot;abcddcba&quot;,&quot;slls&quot;,&quot;llssssll&quot;]

Example 2:
Input: [&quot;bat&quot;,&quot;tab&quot;,&quot;cat&quot;]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are [&quot;battab&quot;,&quot;tabbat&quot;]


*/
pub struct Solution {}
impl Solution {
    pub fn palindrome_pairs(words: Vec<String>) -> Vec<Vec<i32>> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::palindrome_pairs(0));
  println!("Pass test cases!");
}
