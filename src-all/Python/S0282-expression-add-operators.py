"""
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:
Input: num = &quot;123&quot;, target = 6
Output: [&quot;1+2+3&quot;, &quot;1*2*3&quot;] 

Example 2:
Input: num = &quot;232&quot;, target = 8
Output: [&quot;2*3+2&quot;, &quot;2+3*2&quot;]

Example 3:
Input: num = &quot;105&quot;, target = 5
Output: [&quot;1*0+5&quot;,&quot;10-5&quot;]

Example 4:
Input: num = &quot;00&quot;, target = 0
Output: [&quot;0+0&quot;, &quot;0-0&quot;, &quot;0*0&quot;]

Example 5:
Input: num = &quot;3456237490&quot;, target = 9191
Output: []

 
Constraints:
	0 <= num.length <= 10
	num only contain digits.


"""
from typing import List
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().addOperators(0) == 0

