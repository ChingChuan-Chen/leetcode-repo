/*
Given a non-empty string, encode the string such that its encoded length is the shortest.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.

Note:
	k will be a positive integer and encoded string will not be empty or have extra space.
	You may assume that the input string contains only lowercase English letters. The string&#39;s length is at most 160.
	If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them is fine.

 

Example 1:
Input: &quot;aaa&quot;
Output: &quot;aaa&quot;
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.

 

Example 2:
Input: &quot;aaaaa&quot;
Output: &quot;5[a]&quot;
Explanation: &quot;5[a]&quot; is shorter than &quot;aaaaa&quot; by 1 character.

 

Example 3:
Input: &quot;aaaaaaaaaa&quot;
Output: &quot;10[a]&quot;
Explanation: &quot;a9[a]&quot; or &quot;9[a]a&quot; are also valid solutions, both of them have the same length = 5, which is the same as &quot;10[a]&quot;.

 

Example 4:
Input: &quot;aabcaabcd&quot;
Output: &quot;2[aabc]d&quot;
Explanation: &quot;aabc&quot; occurs twice, so one answer can be &quot;2[aabc]d&quot;.

 

Example 5:
Input: &quot;abbbabbbcabbbabbbc&quot;
Output: &quot;2[2[abbb]c]&quot;
Explanation: &quot;abbbabbbc&quot; occurs twice, but &quot;abbbabbbc&quot; can also be encoded to &quot;2[abbb]c&quot;, so one answer can be &quot;2[2[abbb]c]&quot;.

 

*/
pub struct Solution {}
impl Solution {
    pub fn encode(s: String) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::encode(0));
  println!("Pass test cases!");
}
