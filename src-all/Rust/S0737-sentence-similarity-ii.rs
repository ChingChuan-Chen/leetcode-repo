/*
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = [&quot;great&quot;, &quot;acting&quot;, &quot;skills&quot;] and words2 = [&quot;fine&quot;, &quot;drama&quot;, &quot;talent&quot;] are similar, if the similar word pairs are pairs = [[&quot;great&quot;, &quot;good&quot;], [&quot;fine&quot;, &quot;good&quot;], [&quot;acting&quot;,&quot;drama&quot;], [&quot;skills&quot;,&quot;talent&quot;]].

Note that the similarity relation is transitive. For example, if &quot;great&quot; and &quot;good&quot; are similar, and &quot;fine&quot; and &quot;good&quot; are similar, then &quot;great&quot; and &quot;fine&quot; are similar.

Similarity is also symmetric. For example, &quot;great&quot; and &quot;fine&quot; being similar is the same as &quot;fine&quot; and &quot;great&quot; being similar.

Also, a word is always similar with itself. For example, the sentences words1 = [&quot;great&quot;], words2 = [&quot;great&quot;], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = [&quot;great&quot;] can never be similar to words2 = [&quot;doubleplus&quot;,&quot;good&quot;].

Note:
	The length of words1 and words2 will not exceed 1000.
	The length of pairs will not exceed 2000.
	The length of each pairs[i] will be 2.
	The length of each words[i] and pairs[i][j] will be in the range [1, 20].

 

*/
pub struct Solution {}
impl Solution {
    pub fn are_sentences_similar_two(words1: Vec<String>, words2: Vec<String>, pairs: Vec<Vec<String>>) -> bool {
        
    }
}

fn main() {
  assert_eq!(0, Solution::are_sentences_similar_two(0));
  println!("Pass test cases!");
}
