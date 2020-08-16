/*
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string &quot;&quot;. If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:
Input: 
S = &quot;abcdebdde&quot;, T = &quot;bde&quot;
Output: &quot;bcde&quot;
Explanation: 
&quot;bcde&quot; is the answer because it occurs before &quot;bdde&quot; which has the same length.
&quot;deb&quot; is not a smaller window because the elements of T in the window must occur in order.

 

Note:
	All the strings in the input will only contain lowercase letters.
	The length of S will be in the range [1, 20000].
	The length of T will be in the range [1, 100].

 
*/
pub struct Solution {}
impl Solution {
    pub fn min_window(s: String, t: String) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::min_window(0));
  println!("Pass test cases!");
}
