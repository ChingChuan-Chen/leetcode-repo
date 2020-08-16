"""
Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

 
Example 1:
Input: s = &quot;a0b1c2&quot;
Output: &quot;0a1b2c&quot;
Explanation: No two adjacent characters have the same type in &quot;0a1b2c&quot;. &quot;a0b1c2&quot;, &quot;0a1b2c&quot;, &quot;0c2a1b&quot; are also valid permutations.

Example 2:
Input: s = &quot;leetcode&quot;
Output: &quot;&quot;
Explanation: &quot;leetcode&quot; has only characters so we cannot separate them by digits.

Example 3:
Input: s = &quot;1229857369&quot;
Output: &quot;&quot;
Explanation: &quot;1229857369&quot; has only digits so we cannot separate them by characters.

Example 4:
Input: s = &quot;covid2019&quot;
Output: &quot;c2o0v1i9d&quot;

Example 5:
Input: s = &quot;ab123&quot;
Output: &quot;1a2b3&quot;

 
Constraints:
	1 <= s.length <= 500
	s consists of only lowercase English letters and/or digits.


"""
class Solution:
    def reformat(self, s: str) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().reformat(0) == 0

