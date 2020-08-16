"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:
Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:
Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

"""
from typing import List
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        
        pass


if __name__ == '__main__':
    assert Solution().diffWaysToCompute(0) == 0

