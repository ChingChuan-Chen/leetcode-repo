"""
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

 
Example 1:
Input: arr = [&quot;un&quot;,&quot;iq&quot;,&quot;ue&quot;]
Output: 4
Explanation: All possible concatenations are &quot;&quot;,&quot;un&quot;,&quot;iq&quot;,&quot;ue&quot;,&quot;uniq&quot; and &quot;ique&quot;.
Maximum length is 4.

Example 2:
Input: arr = [&quot;cha&quot;,&quot;r&quot;,&quot;act&quot;,&quot;ers&quot;]
Output: 6
Explanation: Possible solutions are &quot;chaers&quot; and &quot;acters&quot;.

Example 3:
Input: arr = [&quot;abcdefghijklmnopqrstuvwxyz&quot;]
Output: 26

 
Constraints:
	1 <= arr.length <= 16
	1 <= arr[i].length <= 26
	arr[i] contains only lower case English letters.


"""
from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().maxLength(0) == 0

