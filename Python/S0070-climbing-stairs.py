"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
	1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1, 2]
        if n >= 3:
            for i in range(2, n):
                arr.append(arr[i - 2] + arr[i - 1])
        return arr[n - 1]


if __name__ == '__main__':
    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(4) == 5
    assert Solution().climbStairs(5) == 8
    assert Solution().climbStairs(6) == 13
    assert Solution().climbStairs(7) == 21
    assert Solution().climbStairs(8) == 34
