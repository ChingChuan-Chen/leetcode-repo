/*
A string of &#39;0&#39;s and &#39;1&#39;s is monotone increasing if it consists of some number of &#39;0&#39;s (possibly 0), followed by some number of &#39;1&#39;s (also possibly 0.)

We are given a string S of &#39;0&#39;s and &#39;1&#39;s, and we may flip any &#39;0&#39; to a &#39;1&#39; or a &#39;1&#39; to a &#39;0&#39;.

Return the minimum number of flips to make S monotone increasing.

 

Example 1:
Input: &quot;00110&quot;
Output: 1
Explanation: We flip the last digit to get 00111.

Example 2:
Input: &quot;010110&quot;
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.

Example 3:
Input: &quot;00011000&quot;
Output: 2
Explanation: We flip to get 00000000.

 

Note:
	1 <= S.length <= 20000
	S only consists of &#39;0&#39; and &#39;1&#39; characters.


*/
pub struct Solution {}
impl Solution {
    pub fn min_flips_mono_incr(s: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::min_flips_mono_incr(0));
  println!("Pass test cases!");
}
