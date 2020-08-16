/*
Given a string s formed by digits (&#39;0&#39; - &#39;9&#39;) and &#39;#&#39; . We want to map s to English lowercase characters as follows:

	Characters (&#39;a&#39; to &#39;i&#39;) are represented by (&#39;1&#39; to &#39;9&#39;) respectively.
	Characters (&#39;j&#39; to &#39;z&#39;) are represented by (&#39;10#&#39; to &#39;26#&#39;) respectively. 

Return the string formed after mapping.

It&#39;s guaranteed that a unique mapping will always exist.

 
Example 1:
Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:
Input: s = "1326#"
Output: "acz"

Example 3:
Input: s = "25#"
Output: "y"

Example 4:
Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"

 
Constraints:
	1 <= s.length <= 1000
	s[i] only contains digits letters (&#39;0&#39;-&#39;9&#39;) and &#39;#&#39; letter.
	s will be valid string such that mapping is always possible.

*/
pub struct Solution {}
impl Solution {
    pub fn freq_alphabets(s: String) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::freq_alphabets(0));
  println!("Pass test cases!");
}
