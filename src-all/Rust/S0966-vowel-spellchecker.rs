/*
Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

	Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.

	
		Example: wordlist = [&quot;yellow&quot;], query = &quot;YellOw&quot;: correct = &quot;yellow&quot;
		Example: wordlist = [&quot;Yellow&quot;], query = &quot;yellow&quot;: correct = &quot;Yellow&quot;
		Example: wordlist = [&quot;yellow&quot;], query = &quot;yellow&quot;: correct = &quot;yellow&quot;
	
	
	Vowel Errors: If after replacing the vowels (&#39;a&#39;, &#39;e&#39;, &#39;i&#39;, &#39;o&#39;, &#39;u&#39;) of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
	
		Example: wordlist = [&quot;YellOw&quot;], query = &quot;yollow&quot;: correct = &quot;YellOw&quot;
		Example: wordlist = [&quot;YellOw&quot;], query = &quot;yeellow&quot;: correct = &quot;&quot; (no match)
		Example: wordlist = [&quot;YellOw&quot;], query = &quot;yllw&quot;: correct = &quot;&quot; (no match)
	
	

In addition, the spell checker operates under the following precedence rules:

	When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
	When the query matches a word up to capitlization, you should return the first such match in the wordlist.
	When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
	If the query has no matches in the wordlist, you should return the empty string.

Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

 

Example 1:
Input: wordlist = [&quot;KiTe&quot;,&quot;kite&quot;,&quot;hare&quot;,&quot;Hare&quot;], queries = [&quot;kite&quot;,&quot;Kite&quot;,&quot;KiTe&quot;,&quot;Hare&quot;,&quot;HARE&quot;,&quot;Hear&quot;,&quot;hear&quot;,&quot;keti&quot;,&quot;keet&quot;,&quot;keto&quot;]
Output: [&quot;kite&quot;,&quot;KiTe&quot;,&quot;KiTe&quot;,&quot;Hare&quot;,&quot;hare&quot;,&quot;&quot;,&quot;&quot;,&quot;KiTe&quot;,&quot;&quot;,&quot;KiTe&quot;]

 

Note:
	1 <= wordlist.length <= 5000
	1 <= queries.length <= 5000
	1 <= wordlist[i].length <= 7
	1 <= queries[i].length <= 7
	All strings in wordlist and queries consist only of english letters.


*/
pub struct Solution {}
impl Solution {
    pub fn spellchecker(wordlist: Vec<String>, queries: Vec<String>) -> Vec<String> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::spellchecker(0));
  println!("Pass test cases!");
}
