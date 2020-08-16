/*
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:
Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Example 2:
Input: A = "apple apple", B = "banana"
Output: ["banana"]

 

Note:
	0 <= A.length <= 200
	0 <= B.length <= 200
	A and B both contain only spaces and lowercase letters.


*/
pub struct Solution {}
impl Solution {
    pub fn uncommon_from_sentences(a: String, b: String) -> Vec<String> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::uncommon_from_sentences(0));
  println!("Pass test cases!");
}
