/*
Return the largest possible k such that there exists a_1, a_2, ..., a_k such that:

	Each a_i is a non-empty string;
	Their concatenation a_1 + a_2 + ... + a_k is equal to text;
	For all 1 <= i <= k,  a_i = a_{k+1 - i}.

 
Example 1:
Input: text = &quot;ghiabcdefhelloadamhelloabcdefghi&quot;
Output: 7
Explanation: We can split the string on &quot;(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)&quot;.

Example 2:
Input: text = &quot;merchant&quot;
Output: 1
Explanation: We can split the string on &quot;(merchant)&quot;.

Example 3:
Input: text = &quot;antaprezatepzapreanta&quot;
Output: 11
Explanation: We can split the string on &quot;(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)&quot;.

Example 4:
Input: text = &quot;aaa&quot;
Output: 3
Explanation: We can split the string on &quot;(a)(a)(a)&quot;.

 
Constraints:
	text consists only of lowercase English characters.
	1 <= text.length <= 1000

*/
pub struct Solution {}
impl Solution {
    pub fn longest_decomposition(text: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::longest_decomposition(0));
  println!("Pass test cases!");
}
