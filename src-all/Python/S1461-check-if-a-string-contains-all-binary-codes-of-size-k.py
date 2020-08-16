"""
Given a binary string s and an integer k.

Return True if every binary code of length k is a substring of s. Otherwise, return False.

 
Example 1:
Input: s = &quot;00110110&quot;, k = 2
Output: true
Explanation: The binary codes of length 2 are &quot;00&quot;, &quot;01&quot;, &quot;10&quot; and &quot;11&quot;. They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.

Example 2:
Input: s = &quot;00110&quot;, k = 2
Output: true

Example 3:
Input: s = &quot;0110&quot;, k = 1
Output: true
Explanation: The binary codes of length 1 are &quot;0&quot; and &quot;1&quot;, it is clear that both exist as a substring. 

Example 4:
Input: s = &quot;0110&quot;, k = 2
Output: false
Explanation: The binary code &quot;00&quot; is of length 2 and doesn&#39;t exist in the array.

Example 5:
Input: s = &quot;0000000001011100&quot;, k = 4
Output: false

 
Constraints:
	1 <= s.length <= 5 * 10^5
	s consists of 0&#39;s and 1&#39;s only.
	1 <= k <= 20


"""
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().hasAllCodes(0) == 0

