/*
A string is called happy if it does not have any of the strings &#39;aaa&#39;, &#39;bbb&#39; or &#39;ccc&#39; as a substring.

Given three integers a, b and c, return any string s, which satisfies following conditions:

	s is happy and longest possible.
	s contains at most a occurrences of the letter &#39;a&#39;, at most b occurrences of the letter &#39;b&#39; and at most c occurrences of the letter &#39;c&#39;.
	s will only contain &#39;a&#39;, &#39;b&#39; and &#39;c&#39; letters.

If there is no such string s return the empty string "".

 
Example 1:
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

Example 2:
Input: a = 2, b = 2, c = 1
Output: "aabbc"

Example 3:
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It&#39;s the only correct answer in this case.

 
Constraints:
	0 <= a, b, c <= 100
	a + b + c > 0


*/
pub struct Solution {}
impl Solution {
    pub fn longest_diverse_string(a: i32, b: i32, c: i32) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::longest_diverse_string(0));
  println!("Pass test cases!");
}
