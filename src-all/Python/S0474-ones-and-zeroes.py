"""
Given an array, strs, with strings consisting of only 0s and 1s. Also two integers m and n.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

 
Example 1:
Input: strs = [&quot;10&quot;,&quot;0001&quot;,&quot;111001&quot;,&quot;1&quot;,&quot;0&quot;], m = 5, n = 3
Output: 4
Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are &quot;10&quot;,&quot;0001&quot;,&quot;1&quot;,&quot;0&quot;.

Example 2:
Input: strs = [&quot;10&quot;,&quot;0&quot;,&quot;1&quot;], m = 1, n = 1
Output: 2
Explanation: You could form &quot;10&quot;, but then you&#39;d have nothing left. Better form &quot;0&quot; and &quot;1&quot;.

 
Constraints:
	1 <= strs.length <= 600
	1 <= strs[i].length <= 100
	strs[i] consists only of digits &#39;0&#39; and &#39;1&#39;.
	1 <= m, n <= 100


"""
from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().findMaxForm(0) == 0

