/*
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.
 
Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As &#39;h&#39; comes before &#39;l&#39; in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As &#39;d&#39; comes after &#39;l&#39; in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because &#39;l&#39; > &#39;&empty;&#39;, where &#39;&empty;&#39; is defined as the blank character which is less than any other character (More info).

 
Constraints:
	1 <= words.length <= 100
	1 <= words[i].length <= 20
	order.length == 26
	All characters in words[i] and order are English lowercase letters.


*/
pub struct Solution {}
impl Solution {
    pub fn is_alien_sorted(words: Vec<String>, order: String) -> bool {
        
    }
}

fn main() {
  assert_eq!(0, Solution::is_alien_sorted(0));
  println!("Pass test cases!");
}
