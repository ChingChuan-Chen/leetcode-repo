/*
With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:

	word contains the first letter of puzzle.
	For each letter in word, that letter is in puzzle.
	For example, if the puzzle is &quot;abcdefg&quot;, then valid words are &quot;faced&quot;, &quot;cabbage&quot;, and &quot;baggage&quot;; while invalid words are &quot;beefed&quot; (doesn&#39;t include &quot;a&quot;) and &quot;based&quot; (includes &quot;s&quot; which isn&#39;t in the puzzle).

Return an array answer, where answer[i] is the number of words in the given word list words that are valid with respect to the puzzle puzzles[i].
 
Example :

Input: 
words = [&quot;aaaa&quot;,&quot;asas&quot;,&quot;able&quot;,&quot;ability&quot;,&quot;actt&quot;,&quot;actor&quot;,&quot;access&quot;], 
puzzles = [&quot;aboveyz&quot;,&quot;abrodyz&quot;,&quot;abslute&quot;,&quot;absoryz&quot;,&quot;actresz&quot;,&quot;gaswxyz&quot;]
Output: [1,1,3,2,4,0]
Explanation:
1 valid word for &quot;aboveyz&quot; : &quot;aaaa&quot; 
1 valid word for &quot;abrodyz&quot; : &quot;aaaa&quot;
3 valid words for &quot;abslute&quot; : &quot;aaaa&quot;, &quot;asas&quot;, &quot;able&quot;
2 valid words for &quot;absoryz&quot; : &quot;aaaa&quot;, &quot;asas&quot;
4 valid words for &quot;actresz&quot; : &quot;aaaa&quot;, &quot;asas&quot;, &quot;actt&quot;, &quot;access&quot;
There&#39;re no valid words for &quot;gaswxyz&quot; cause none of the words in the list contains letter &#39;g&#39;.

 
Constraints:
	1 <= words.length <= 10^5
	4 <= words[i].length <= 50
	1 <= puzzles.length <= 10^4
	puzzles[i].length == 7
	words[i][j], puzzles[i][j] are English lowercase letters.
	Each puzzles[i] doesn&#39;t contain repeated characters.


*/
pub struct Solution {}
impl Solution {
    pub fn find_num_of_valid_words(words: Vec<String>, puzzles: Vec<String>) -> Vec<i32> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::find_num_of_valid_words(0));
  println!("Pass test cases!");
}
