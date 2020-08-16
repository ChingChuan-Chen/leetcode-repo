/*
A happy string is a string that:

	consists only of letters of the set [&#39;a&#39;, &#39;b&#39;, &#39;c&#39;].
	s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).

For example, strings &quot;abc&quot;, &quot;ac&quot;, &quot;b&quot; and &quot;abcbabcbcb&quot; are all happy strings and strings &quot;aa&quot;, &quot;baa&quot; and &quot;ababbc&quot; are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

 
Example 1:
Input: n = 1, k = 3
Output: &quot;c&quot;
Explanation: The list [&quot;a&quot;, &quot;b&quot;, &quot;c&quot;] contains all happy strings of length 1. The third string is &quot;c&quot;.

Example 2:
Input: n = 1, k = 4
Output: &quot;&quot;
Explanation: There are only 3 happy strings of length 1.

Example 3:
Input: n = 3, k = 9
Output: &quot;cab&quot;
Explanation: There are 12 different happy string of length 3 [&quot;aba&quot;, &quot;abc&quot;, &quot;aca&quot;, &quot;acb&quot;, &quot;bab&quot;, &quot;bac&quot;, &quot;bca&quot;, &quot;bcb&quot;, &quot;cab&quot;, &quot;cac&quot;, &quot;cba&quot;, &quot;cbc&quot;]. You will find the 9th string = &quot;cab&quot;

Example 4:
Input: n = 2, k = 7
Output: &quot;&quot;

Example 5:
Input: n = 10, k = 100
Output: &quot;abacbabacb&quot;

 
Constraints:
	1 <= n <= 10
	1 <= k <= 100

 
*/
pub struct Solution {}
impl Solution {
    pub fn get_happy_string(n: i32, k: i32) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::get_happy_string(0));
  println!("Pass test cases!");
}
