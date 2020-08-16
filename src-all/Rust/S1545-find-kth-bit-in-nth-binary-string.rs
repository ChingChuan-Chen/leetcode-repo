/*
Given two positive integers n and k, the binary string  Sn is formed as follows:

	S1 = &quot;0&quot;
	Si = Si-1 + &quot;1&quot; + reverse(invert(Si-1)) for i > 1

Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first 4 strings in the above sequence are:

	S1 = &quot;0&quot;
	S2 = &quot;011&quot;
	S3 = &quot;0111001&quot;
	S4 = &quot;011100110110001&quot;

Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

 
Example 1:
Input: n = 3, k = 1
Output: &quot;0&quot;
Explanation: S3 is &quot;0111001&quot;. The first bit is &quot;0&quot;.

Example 2:
Input: n = 4, k = 11
Output: &quot;1&quot;
Explanation: S4 is &quot;011100110110001&quot;. The 11th bit is &quot;1&quot;.

Example 3:
Input: n = 1, k = 1
Output: &quot;0&quot;

Example 4:
Input: n = 2, k = 3
Output: &quot;1&quot;

 
Constraints:
	1 <= n <= 20
	1 <= k <= 2n - 1

*/
pub struct Solution {}
impl Solution {
    pub fn find_kth_bit(n: i32, k: i32) -> char {
        
    }
}

fn main() {
  assert_eq!(0, Solution::find_kth_bit(0));
  println!("Pass test cases!");
}
