/*
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:
Input: 
s = &quot;abcxyz123&quot;
dict = [&quot;abc&quot;,&quot;123&quot;]
Output:
&quot;<b>abc</b>xyz<b>123</b>&quot;

 

Example 2:
Input: 
s = &quot;aaabbcc&quot;
dict = [&quot;aaa&quot;,&quot;aab&quot;,&quot;bc&quot;]
Output:
&quot;<b>aaabbc</b>c&quot;

 

Constraints:
	The given dict won&#39;t contain duplicates, and its length won&#39;t exceed 100.
	All the strings in input have length in range [1, 1000].

Note: This question is the same as 758: https://leetcode.com/problems/bold-words-in-string/

*/
pub struct Solution {}
impl Solution {
    pub fn add_bold_tag(s: String, dict: Vec<String>) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::add_bold_tag(0));
  println!("Pass test cases!");
}
