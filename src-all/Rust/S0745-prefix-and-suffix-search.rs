/*
Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix). It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

Examples:

Input:
WordFilter([&quot;apple&quot;])
WordFilter.f(&quot;a&quot;, &quot;e&quot;) // returns 0
WordFilter.f(&quot;b&quot;, &quot;&quot;) // returns -1

 

Note:
	words has length in range [1, 15000].
	For each test case, up to words.length queries WordFilter.f may be made.
	words[i] has length in range [1, 10].
	prefix, suffix have lengths in range [0, 10].
	words[i] and prefix, suffix queries consist of lowercase letters only.

 

*/
pub struct Solution {}
struct WordFilter {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl WordFilter {

    fn new(words: Vec<String>) -> Self {
        
    }
    
    fn f(&self, prefix: String, suffix: String) -> i32 {
        
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * let obj = WordFilter::new(words);
 * let ret_1: i32 = obj.f(prefix, suffix);
 */

fn main() {
  assert_eq!(0, Solution::new(0));
  println!("Pass test cases!");
}
