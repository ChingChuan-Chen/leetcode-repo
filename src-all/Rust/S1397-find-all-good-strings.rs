/*
Given the strings s1 and s2 of size n, and the string evil. Return the number of good strings.

A good string has size n, it is alphabetically greater than or equal to s1, it is alphabetically smaller than or equal to s2, and it does not contain the string evil as a substring. Since the answer can be a huge number, return this modulo 10^9 + 7.

 
Example 1:
Input: n = 2, s1 = &quot;aa&quot;, s2 = &quot;da&quot;, evil = &quot;b&quot;
Output: 51 
Explanation: There are 25 good strings starting with &#39;a&#39;: &quot;aa&quot;,&quot;ac&quot;,&quot;ad&quot;,...,&quot;az&quot;. Then there are 25 good strings starting with &#39;c&#39;: &quot;ca&quot;,&quot;cc&quot;,&quot;cd&quot;,...,&quot;cz&quot; and finally there is one good string starting with &#39;d&#39;: &quot;da&quot;. 

Example 2:
Input: n = 8, s1 = &quot;leetcode&quot;, s2 = &quot;leetgoes&quot;, evil = &quot;leet&quot;
Output: 0 
Explanation: All strings greater than or equal to s1 and smaller than or equal to s2 start with the prefix &quot;leet&quot;, therefore, there is not any good string.

Example 3:
Input: n = 2, s1 = &quot;gx&quot;, s2 = &quot;gz&quot;, evil = &quot;x&quot;
Output: 2

 
Constraints:
	s1.length == n
	s2.length == n
	s1 <= s2
	1 <= n <= 500
	1 <= evil.length <= 50
	All strings consist of lowercase English letters.


*/
pub struct Solution {}
impl Solution {
    pub fn find_good_strings(n: i32, s1: String, s2: String, evil: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::find_good_strings(0));
  println!("Pass test cases!");
}
