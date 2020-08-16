/*
Design an Iterator class, which has:

	A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
	A function next() that returns the next combination of length combinationLength in lexicographical order.
	A function hasNext() that returns True if and only if there exists a next combination.

 

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false

 
Constraints:
	1 <= combinationLength <= characters.length <= 15
	There will be at most 10^4 function calls per test.
	It&#39;s guaranteed that all calls of the function next are valid.


*/
pub struct Solution {}
struct CombinationIterator {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl CombinationIterator {

    fn new(characters: String, combinationLength: i32) -> Self {
        
    }
    
    fn next(&self) -> String {
        
    }
    
    fn has_next(&self) -> bool {
        
    }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * let obj = CombinationIterator::new(characters, combinationLength);
 * let ret_1: String = obj.next();
 * let ret_2: bool = obj.has_next();
 */

fn main() {
  assert_eq!(0, Solution::new(0));
  println!("Pass test cases!");
}
