/*
Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

For example, if the list of words is [&quot;time&quot;, &quot;me&quot;, &quot;bell&quot;], we can write it as S = &quot;time#bell#&quot; and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference string from that index until we reach a &quot;#&quot; character.

What is the length of the shortest reference string S possible that encodes the given words?

Example:

Input: words = [&quot;time&quot;, &quot;me&quot;, &quot;bell&quot;]
Output: 10
Explanation: S = &quot;time#bell#&quot; and indexes = [0, 2, 5].

 

Note:
	1 <= words.length <= 2000.
	1 <= words[i].length <= 7.
	Each word has only lowercase letters.


*/
pub struct Solution {}
impl Solution {
    pub fn minimum_length_encoding(words: Vec<String>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::minimum_length_encoding(0));
  println!("Pass test cases!");
}
