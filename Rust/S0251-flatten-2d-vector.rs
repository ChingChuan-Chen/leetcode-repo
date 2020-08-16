/*
Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.

 

Example:

Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false

 

Notes:

	Please remember to RESET your class variables declared in Vector2D, as static/class variables are persisted across multiple test cases. Please see here for more details.
	You may assume that next() call will always be valid, that is, there will be at least a next element in the 2d vector when next() is called.

 

Follow up:
As an added challenge, try to code it using only iterators in C++ or iterators in Java.

*/
pub struct Solution {}
struct Vector2D {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Vector2D {

    fn new(v: Vec<Vec<i32>>) -> Self {
        
    }
    
    fn next(&self) -> i32 {
        
    }
    
    fn has_next(&self) -> bool {
        
    }
}

/**
 * Your Vector2D object will be instantiated and called as such:
 * let obj = Vector2D::new(v);
 * let ret_1: i32 = obj.next();
 * let ret_2: bool = obj.has_next();
 */

fn main() {
  assert_eq!(0, Solution::new(0));
  println!("Pass test cases!");
}
