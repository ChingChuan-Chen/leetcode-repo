/*
You should design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

	WordDictionary() Initializes the object.
	void addWord(word) adds word to the data structure, it can be matched later.
	bool search(word) returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots &#39;.&#39; where dots can be matched with any letter.

 
Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

 
Constraints:
	1 <= word.length <= 500
	word in addWord consists lower-case English letters.
	word in search consist of  &#39;.&#39; or lower-case English letters.
	At most 50000 calls will be made to addWord and search .


*/
pub struct Solution {}
struct WordDictionary {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl WordDictionary {

    /** Initialize your data structure here. */
    fn new() -> Self {
        
    }
    
    /** Adds a word into the data structure. */
    fn add_word(&self, word: String) {
        
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    fn search(&self, word: String) -> bool {
        
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * let obj = WordDictionary::new();
 * obj.add_word(word);
 * let ret_2: bool = obj.search(word);
 */

fn main() {
  assert_eq!(0, Solution::new(0));
  println!("Pass test cases!");
}
