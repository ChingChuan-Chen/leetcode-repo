/*
Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction &quot;A&quot;, your car does the following: position += speed, speed *= 2.

When you get an instruction &quot;R&quot;, your car does the following: if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)

For example, after commands &quot;AAR&quot;, your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.

Now for some target position, say the length of the shortest sequence of instructions to get there.

Example 1:
Input: 
target = 3
Output: 2
Explanation: 
The shortest instruction sequence is &quot;AA&quot;.
Your position goes from 0->1->3.

Example 2:
Input: 
target = 6
Output: 5
Explanation: 
The shortest instruction sequence is &quot;AAARA&quot;.
Your position goes from 0->1->3->7->7->6.

 

Note: 

	1 <= target <= 10000.


*/
pub struct Solution {}
impl Solution {
    pub fn racecar(target: i32) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::racecar(0));
  println!("Pass test cases!");
}
