"""
Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false

Follow up:
Could you do it without using any loop / recursion?
"""
import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        x = math.log(n) / math.log(3)
        epsilon = 1e-10
        return (x+epsilon) % 1 <= 2*epsilon


if __name__ == '__main__':
    assert Solution().isPowerOfThree(27) == True
    assert Solution().isPowerOfThree(0) == False
    assert Solution().isPowerOfThree(1) == True
    assert Solution().isPowerOfThree(9) == True
    assert Solution().isPowerOfThree(45) == False
    assert Solution().isPowerOfThree(531440) == False
    assert Solution().isPowerOfThree(177146) == False
    assert Solution().isPowerOfThree(177147) == True
    assert Solution().isPowerOfThree(1594322) == False
    assert Solution().isPowerOfThree(1594323) == True
    assert Solution().isPowerOfThree(4782968) == False
    assert Solution().isPowerOfThree(4782969) == True
    assert Solution().isPowerOfThree(4782970) == False