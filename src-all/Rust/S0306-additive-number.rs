/*
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits &#39;0&#39;-&#39;9&#39;, write a function to determine if it&#39;s an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 
Example 1:
Input: &quot;112358&quot;
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

Example 2:
Input: &quot;199100199&quot;
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199

 
Constraints:
	num consists only of digits &#39;0&#39;-&#39;9&#39;.
	1 <= num.length <= 35

Follow up:
How would you handle overflow for very large input integers?

*/
pub struct Solution {}
impl Solution {
    pub fn is_additive_number(num: String) -> bool {
        
    }
}

fn main() {
  assert_eq!(0, Solution::is_additive_number(0));
  println!("Pass test cases!");
}
