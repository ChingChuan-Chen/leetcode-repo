"""
Balanced strings are those who have equal quantity of &#39;L&#39; and &#39;R&#39; characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 
Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of &#39;L&#39; and &#39;R&#39;.

Example 2:
Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of &#39;L&#39; and &#39;R&#39;.

Example 3:
Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

Example 4:
Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of &#39;L&#39; and &#39;R&#39;

 
Constraints:
	1 <= s.length <= 1000
	s[i] = &#39;L&#39; or &#39;R&#39;


"""
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().balancedStringSplit(0) == 0

