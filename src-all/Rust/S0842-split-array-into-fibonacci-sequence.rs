/*
Given a string S of digits, such as S = &quot;123456579&quot;, we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

	0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
	F.length >= 3;
	and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.

Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:
Input: &quot;123456579&quot;
Output: [123,456,579]

Example 2:
Input: &quot;11235813&quot;
Output: [1,1,2,3,5,8,13]

Example 3:
Input: &quot;112358130&quot;
Output: []
Explanation: The task is impossible.

Example 4:
Input: &quot;0123&quot;
Output: []
Explanation: Leading zeroes are not allowed, so &quot;01&quot;, &quot;2&quot;, &quot;3&quot; is not valid.

Example 5:
Input: &quot;1101111&quot;
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.

Note: 

	1 <= S.length <= 200
	S contains only digits.


*/
pub struct Solution {}
impl Solution {
    pub fn split_into_fibonacci(s: String) -> Vec<i32> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::split_into_fibonacci(0));
  println!("Pass test cases!");
}
