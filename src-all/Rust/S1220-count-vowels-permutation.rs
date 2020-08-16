/*
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

	Each character is a lower case vowel (&#39;a&#39;, &#39;e&#39;, &#39;i&#39;, &#39;o&#39;, &#39;u&#39;)
	Each vowel &#39;a&#39; may only be followed by an &#39;e&#39;.
	Each vowel &#39;e&#39; may only be followed by an &#39;a&#39; or an &#39;i&#39;.
	Each vowel &#39;i&#39; may not be followed by another &#39;i&#39;.
	Each vowel &#39;o&#39; may only be followed by an &#39;i&#39; or a &#39;u&#39;.
	Each vowel &#39;u&#39; may only be followed by an &#39;a&#39;.

Since the answer may be too large, return it modulo 10^9 + 7.

 
Example 1:
Input: n = 1
Output: 5
Explanation: All possible strings are: &quot;a&quot;, &quot;e&quot;, &quot;i&quot; , &quot;o&quot; and &quot;u&quot;.

Example 2:
Input: n = 2
Output: 10
Explanation: All possible strings are: &quot;ae&quot;, &quot;ea&quot;, &quot;ei&quot;, &quot;ia&quot;, &quot;ie&quot;, &quot;io&quot;, &quot;iu&quot;, &quot;oi&quot;, &quot;ou&quot; and &quot;ua&quot;.

Example 3: 

Input: n = 5
Output: 68

 
Constraints:
	1 <= n <= 2 * 10^4


*/
pub struct Solution {}
impl Solution {
    pub fn count_vowel_permutation(n: i32) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::count_vowel_permutation(0));
  println!("Pass test cases!");
}
