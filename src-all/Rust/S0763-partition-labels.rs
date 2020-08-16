/*
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:
Input: S = &quot;ababcbacadefegdehijhklij&quot;
Output: [9,7,8]
Explanation:
The partition is &quot;ababcbaca&quot;, &quot;defegde&quot;, &quot;hijhklij&quot;.
This is a partition so that each letter appears in at most one part.
A partition like &quot;ababcbacadefegde&quot;, &quot;hijhklij&quot; is incorrect, because it splits S into less parts.

 

Note:
	S will have length in range [1, 500].
	S will consist of lowercase English letters (&#39;a&#39; to &#39;z&#39;) only.

 

*/
pub struct Solution {}
impl Solution {
    pub fn partition_labels(s: String) -> Vec<i32> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::partition_labels(0));
  println!("Pass test cases!");
}
