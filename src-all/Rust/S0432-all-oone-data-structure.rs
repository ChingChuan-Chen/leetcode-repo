/*
Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key  with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".

Challenge: Perform all these in O(1) time complexity.

*/
pub struct Solution {}
struct AllOne {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl AllOne {

    /** Initialize your data structure here. */
    fn new() -> Self {
        
    }
    
    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    fn inc(&self, key: String) {
        
    }
    
    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    fn dec(&self, key: String) {
        
    }
    
    /** Returns one of the keys with maximal value. */
    fn get_max_key(&self) -> String {
        
    }
    
    /** Returns one of the keys with Minimal value. */
    fn get_min_key(&self) -> String {
        
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * let obj = AllOne::new();
 * obj.inc(key);
 * obj.dec(key);
 * let ret_3: String = obj.get_max_key();
 * let ret_4: String = obj.get_min_key();
 */

fn main() {
  assert_eq!(0, Solution::new(0));
  println!("Pass test cases!");
}
