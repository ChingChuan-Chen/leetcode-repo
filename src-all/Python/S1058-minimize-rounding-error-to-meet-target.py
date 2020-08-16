"""
Given an array of prices [p1,p2...,pn] and a target, round each price pi to Roundi(pi) so that the rounded array [Round1(p1),Round2(p2)...,Roundn(pn)] sums to the given target. Each operation Roundi(pi) could be either Floor(pi) or Ceil(pi).

Return the string &quot;-1&quot; if the rounded array is impossible to sum to target. Otherwise, return the smallest rounding error, which is defined as &Sigma; |Roundi(pi) - (pi)| for i from 1 to n, as a string with three places after the decimal.

 

Example 1:
Input: prices = [&quot;0.700&quot;,&quot;2.800&quot;,&quot;4.900&quot;], target = 8
Output: &quot;1.000&quot;
Explanation: 
Use Floor, Ceil and Ceil operations to get (0.7 - 0) + (3 - 2.8) + (5 - 4.9) = 0.7 + 0.2 + 0.1 = 1.0 .

Example 2:
Input: prices = [&quot;1.500&quot;,&quot;2.500&quot;,&quot;3.500&quot;], target = 10
Output: &quot;-1&quot;
Explanation: 
It is impossible to meet the target.

 

Note:
	1 <= prices.length <= 500.
	Each string of prices prices[i] represents a real number which is between 0 and 1000 and has exactly 3 decimal places.
	target is between 0 and 1000000.

"""
from typing import List
class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().minimizeError(0) == 0

