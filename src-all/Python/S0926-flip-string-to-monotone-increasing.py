"""
A string of &#39;0&#39;s and &#39;1&#39;s is monotone increasing if it consists of some number of &#39;0&#39;s (possibly 0), followed by some number of &#39;1&#39;s (also possibly 0.)

We are given a string S of &#39;0&#39;s and &#39;1&#39;s, and we may flip any &#39;0&#39; to a &#39;1&#39; or a &#39;1&#39; to a &#39;0&#39;.

Return the minimum number of flips to make S monotone increasing.

 

Example 1:
Input: "00110"
Output: 1
Explanation: We flip the last digit to get 00111.

Example 2:
Input: "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.

Example 3:
Input: "00011000"
Output: 2
Explanation: We flip to get 00000000.

 

Note:
	1 <= S.length <= 20000
	S only consists of &#39;0&#39; and &#39;1&#39; characters.


"""
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().minFlipsMonoIncr(0) == 0

