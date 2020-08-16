/*
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

 

Example 1:
Input:
  s = &quot;barfoothefoobarman&quot;,
  words = [&quot;foo&quot;,&quot;bar&quot;]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are &quot;barfoo&quot; and &quot;foobar&quot; respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:
Input:
  s = &quot;wordgoodgoodgoodbestword&quot;,
  words = [&quot;word&quot;,&quot;good&quot;,&quot;best&quot;,&quot;word&quot;]
Output: []


*/
pub struct Solution {}
impl Solution {
    pub fn find_substring(s: String, words: Vec<String>) -> Vec<i32> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::find_substring(0));
  println!("Pass test cases!");
}
