"""
Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.

 

Example 1:
Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert &#39;c&#39; to &#39;e&#39; then &#39;b&#39; to &#39;d&#39; then &#39;a&#39; to &#39;c&#39;. Note that the order of conversions matter.

Example 2:
Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.

 

Note:
	1 <= str1.length == str2.length <= 10^4
	Both str1 and str2 contain only lowercase English letters.


"""
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().canConvert(0) == 0

