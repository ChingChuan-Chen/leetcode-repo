/*
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string&#39;s length and k will not exceed 104.

Example 1:
Input:
s = &quot;ABAB&quot;, k = 2

Output:
4

Explanation:
Replace the two &#39;A&#39;s with two &#39;B&#39;s or vice versa.

 

Example 2:
Input:
s = &quot;AABABBA&quot;, k = 1

Output:
4

Explanation:
Replace the one &#39;A&#39; in the middle with &#39;B&#39; and form &quot;AABBBBA&quot;.
The substring &quot;BBBB&quot; has the longest repeating letters, which is 4.

 

*/
pub struct Solution {}
impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::character_replacement(0));
  println!("Pass test cases!");
}
