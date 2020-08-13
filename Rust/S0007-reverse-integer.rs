/*
Given a 32-bit signed integer, reverse digits of an integer.

- Example 1:

Input: 123
Output: 321

- Example 2:

Input: -123
Output: -321

- Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only
store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
For the purpose of this problem, assume that your function returns 0
when the reversed integer overflows.
*/
pub struct Solution {}

impl Solution {
	pub fn reverse(x: i32) -> i32 {
		let neg = if x < 0 {
			-1
		} else {
			1
		};

		let mut input = if x < 0 {
			-x
		} else {
			x
		} as i64;
		let mut out = 0i64;
		while input > 0 {
		    out *= 10;
		    out += &input % 10;
		    input /= 10;
		}
		if out > std::i32::MAX as i64 || out < std::i32::MIN as i64 {
			return 0;
		}
		return (out*neg) as i32;
	}
}

fn main() {
  assert_eq!(321, Solution::reverse(123));
  assert_eq!(-321, Solution::reverse(-123));
  assert_eq!(21, Solution::reverse(120));
  assert_eq!(0, Solution::reverse(1534236469));
  println!("Pass test cases!");
}

