/*
Implement the StreamChecker class as follows:

	StreamChecker(words): Constructor, init the data structure with the given words.
	query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.

 

Example:

StreamChecker streamChecker = new StreamChecker([&quot;cd&quot;,&quot;f&quot;,&quot;kl&quot;]); // init the dictionary.
streamChecker.query(&#39;a&#39;);          // return false
streamChecker.query(&#39;b&#39;);          // return false
streamChecker.query(&#39;c&#39;);          // return false
streamChecker.query(&#39;d&#39;);          // return true, because &#39;cd&#39; is in the wordlist
streamChecker.query(&#39;e&#39;);          // return false
streamChecker.query(&#39;f&#39;);          // return true, because &#39;f&#39; is in the wordlist
streamChecker.query(&#39;g&#39;);          // return false
streamChecker.query(&#39;h&#39;);          // return false
streamChecker.query(&#39;i&#39;);          // return false
streamChecker.query(&#39;j&#39;);          // return false
streamChecker.query(&#39;k&#39;);          // return false
streamChecker.query(&#39;l&#39;);          // return true, because &#39;kl&#39; is in the wordlist

 

Note:
	1 <= words.length <= 2000
	1 <= words[i].length <= 2000
	Words will only consist of lowercase English letters.
	Queries will only consist of lowercase English letters.
	The number of queries is at most 40000.


*/
pub struct Solution {}
struct StreamChecker {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl StreamChecker {

    fn new(words: Vec<String>) -> Self {
        
    }
    
    fn query(&self, letter: char) -> bool {
        
    }
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * let obj = StreamChecker::new(words);
 * let ret_1: bool = obj.query(letter);
 */

fn main() {
  assert_eq!(0, Solution::new(0));
  println!("Pass test cases!");
}
