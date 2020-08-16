/*
We are given a personal information string S, which may represent either an email address or a phone number.

We would like to mask this personal information according to the following rules:

1. Email address:

We define a name to be a string of length &ge; 2 consisting of only lowercase letters a-z or uppercase letters A-Z.

An email address starts with a name, followed by the symbol &#39;@&#39;, followed by a name, followed by the dot &#39;.&#39; and followed by a name. 

All email addresses are guaranteed to be valid and in the format of &quot;name1@name2.name3&quot;.

To mask an email, all names must be converted to lowercase and all letters between the first and last letter of the first name must be replaced by 5 asterisks &#39;*&#39;.

2. Phone number:

A phone number is a string consisting of only the digits 0-9 or the characters from the set {&#39;+&#39;, &#39;-&#39;, &#39;(&#39;, &#39;)&#39;, &#39; &#39;}. You may assume a phone number contains 10 to 13 digits.

The last 10 digits make up the local number, while the digits before those make up the country code. Note that the country code is optional. We want to expose only the last 4 digits and mask all other digits.

The local number should be formatted and masked as &quot;***-***-1111&quot;, where 1 represents the exposed digits.

To mask a phone number with country code like &quot;+111 111 111 1111&quot;, we write it in the form &quot;+***-***-***-1111&quot;.  The &#39;+&#39; sign and the first &#39;-&#39; sign before the local number should only exist if there is a country code.  For example, a 12 digit phone number mask should start with &quot;+**-&quot;.

Note that extraneous characters like &quot;(&quot;, &quot;)&quot;, &quot; &quot;, as well as extra dashes or plus signs not part of the above formatting scheme should be removed.

 

Return the correct &quot;mask&quot; of the information provided.

 

Example 1:
Input: &quot;LeetCode@LeetCode.com&quot;
Output: &quot;l*****e@leetcode.com&quot;
Explanation: All names are converted to lowercase, and the letters between the
             first and last letter of the first name is replaced by 5 asterisks.
             Therefore, &quot;leetcode&quot; -> &quot;l*****e&quot;.

Example 2:
Input: &quot;AB@qq.com&quot;
Output: &quot;a*****b@qq.com&quot;
Explanation: There must be 5 asterisks between the first and last letter 
             of the first name &quot;ab&quot;. Therefore, &quot;ab&quot; -> &quot;a*****b&quot;.

Example 3:
Input: &quot;1(234)567-890&quot;
Output: &quot;***-***-7890&quot;
Explanation: 10 digits in the phone number, which means all digits make up the local number.

Example 4:
Input: &quot;86-(10)12345678&quot;
Output: &quot;+**-***-***-5678&quot;
Explanation: 12 digits, 2 digits for country code and 10 digits for local number. 

Notes:

	S.length <= 40.
	Emails have length at least 8.
	Phone numbers have length at least 10.


*/
pub struct Solution {}
impl Solution {
    pub fn mask_pii(s: String) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::mask_pii(0));
  println!("Pass test cases!");
}
