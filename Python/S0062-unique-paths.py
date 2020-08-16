"""
A robot is located at the top-left corner of a m x n grid (marked &#39;Start&#39; in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked &#39;Finish&#39; in the diagram below).

How many possible unique paths are there?

Above is a 7 x 3 grid. How many possible unique paths are there?

 
Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28

 
Constraints:
	1 <= m, n <= 100
	It&#39;s guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.


"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().uniquePaths(0) == 0

