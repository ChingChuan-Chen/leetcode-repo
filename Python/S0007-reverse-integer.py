# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
# Input: 123
# Output: 321
#
#
# Example 2:
# Input: -123
# Output: -321
#
#
# Example 3:
# Input: 120
# Output: 21
#
#  Note:
# Assume we are dealing with an environment which could only store integers with
# in the 32-bit signed integer range: [−231, 231 − 1]. For the purpose of this problem,
# assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        neg = 1
        if x < 0:
            neg = -1
            x *= -1
        out = 0
        while x > 0:
            rem = x % 10
            x //= 10
            out = out * 10 + rem

        if out >= 2**31-1 or out <= -2**31:
            return 0
        return out * neg

if __name__ == '__main__':
    assert Solution().reverse(123) == 321
    assert Solution().reverse(-123) == -321
    assert Solution().reverse(120) == 21
    assert Solution().reverse(123654) == 456321
    assert Solution().reverse(-123654) == -456321
    assert Solution().reverse(1534236469) == 0

