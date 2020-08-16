/*
You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.

Implement the DinnerPlates class:

	DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks.
	void push(int val) pushes the given positive integer val into the leftmost stack with size less than capacity.
	int pop() returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all stacks are empty.
	int popAtStack(int index) returns the value at the top of the stack with the given index and removes it from that stack, and returns -1 if the stack with that given index is empty.

Example:

Input: 
["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
Output: 
[null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

Explanation: 
DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);         // The stacks are now:  2  4
                                           1  3  5
                                           <U+FE48> <U+FE48> <U+FE48>
D.popAtStack(0);   // Returns 2.  The stacks are now:     4
                                                       1  3  5
                                                       <U+FE48> <U+FE48> <U+FE48>
D.push(20);        // The stacks are now: 20  4
                                           1  3  5
                                           <U+FE48> <U+FE48> <U+FE48>
D.push(21);        // The stacks are now: 20  4 21
                                           1  3  5
                                           <U+FE48> <U+FE48> <U+FE48>
D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
                                                        1  3  5
                                                        <U+FE48> <U+FE48> <U+FE48>
D.popAtStack(2);   // Returns 21.  The stacks are now:     4
                                                        1  3  5
                                                        <U+FE48> <U+FE48> <U+FE48> 
D.pop()            // Returns 5.  The stacks are now:      4
                                                        1  3 
                                                        <U+FE48> <U+FE48>  
D.pop()            // Returns 4.  The stacks are now:   1  3 
                                                        <U+FE48> <U+FE48>   
D.pop()            // Returns 3.  The stacks are now:   1 
                                                        <U+FE48>   
D.pop()            // Returns 1.  There are no stacks.
D.pop()            // Returns -1.  There are still no stacks.

 
Constraints:
	1 <= capacity <= 20000
	1 <= val <= 20000
	0 <= index <= 100000
	At most 200000 calls will be made to push, pop, and popAtStack.


*/
pub struct Solution {}
struct DinnerPlates {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl DinnerPlates {

    fn new(capacity: i32) -> Self {
        
    }
    
    fn push(&self, val: i32) {
        
    }
    
    fn pop(&self) -> i32 {
        
    }
    
    fn pop_at_stack(&self, index: i32) -> i32 {
        
    }
}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * let obj = DinnerPlates::new(capacity);
 * obj.push(val);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.pop_at_stack(index);
 */

fn main() {
  assert_eq!(0, Solution::new(0));
  println!("Pass test cases!");
}
