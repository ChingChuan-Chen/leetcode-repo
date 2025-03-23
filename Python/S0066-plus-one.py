"""
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
 Input: [1,2,3]
 Output: [1,2,4]
 Explanation: The array represents the integer 123.

Example 2:
 Input: [4,3,2,1]
 Output: [4,3,2,2]
 Explanation: The array represents the integer 4321.
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        for i in range(len(digits) - 1, -1, -1):
            if carry:
                digits[i] += 1
                carry = False

            if digits[i] > 9:
                digits[i] -= 10
                carry = True
            else:
                break

        if carry:
            digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]
    assert Solution().plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert Solution().plusOne([4, 2, 9, 9]) == [4, 3, 0, 0]
    assert Solution().plusOne([2, 9, 9]) == [3, 0, 0]
    assert Solution().plusOne([0]) == [1]
    assert Solution().plusOne([9, 9, 9]) == [1, 0, 0, 0]
