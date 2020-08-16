/*
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

	push(x) -- Push element x onto stack.
	pop() -- Removes the element on top of the stack.
	top() -- Get the top element.
	getMin() -- Retrieve the minimum element in the stack.

 
Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

 
Constraints:
	Methods pop, top and getMin operations will always be called on non-empty stacks.


*/
pub struct Solution {}
struct MinStack {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {

    /** initialize your data structure here. */
    fn new() -> Self {
        
    }
    
    fn push(&self, x: i32) {
        
    }
    
    fn pop(&self) {
        
    }
    
    fn top(&self) -> i32 {
        
    }
    
    fn get_min(&self) -> i32 {
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * let obj = MinStack::new();
 * obj.push(x);
 * obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: i32 = obj.get_min();
 */

fn main() {
  assert_eq!(0, Solution::new(0));
  println!("Pass test cases!");
}
