"""
Given an array of integers cost and an integer target. Return the maximum integer you can paint under the following rules:

	The cost of painting a digit (i+1) is given by cost[i] (0 indexed).
	The total cost used must be equal to target.
	Integer does not have digits 0.

Since the answer may be too large, return it as string.

If there is no way to paint any integer given the condition, return &quot;0&quot;.

 
Example 1:
Input: cost = [4,3,2,5,6,7,2,5,5], target = 9
Output: &quot;7772&quot;
Explanation:  The cost to paint the digit &#39;7&#39; is 2, and the digit &#39;2&#39; is 3. Then cost(&quot;7772&quot;) = 2*3+ 3*1 = 9. You could also paint &quot;977&quot;, but &quot;7772&quot; is the largest number.
Digit    cost
  1  ->   4
  2  ->   3
  3  ->   2
  4  ->   5
  5  ->   6
  6  ->   7
  7  ->   2
  8  ->   5
  9  ->   5

Example 2:
Input: cost = [7,6,5,5,5,6,8,7,8], target = 12
Output: &quot;85&quot;
Explanation: The cost to paint the digit &#39;8&#39; is 7, and the digit &#39;5&#39; is 5. Then cost(&quot;85&quot;) = 7 + 5 = 12.

Example 3:
Input: cost = [2,4,6,2,4,6,4,4,4], target = 5
Output: &quot;0&quot;
Explanation: It&#39;s not possible to paint any integer with total cost equal to target.

Example 4:
Input: cost = [6,10,15,40,40,40,40,40,40], target = 47
Output: &quot;32211&quot;

 
Constraints:
	cost.length == 9
	1 <= cost[i] <= 5000
	1 <= target <= 5000


"""
from typing import List
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().largestNumber(0) == 0

