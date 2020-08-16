"""
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2.

Note:
	Your returned answers (both index1 and index2) are not zero-based.
	You may assume that each input would have exactly one solution
	and you may not use the same element twice.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while low < high:
            sum = numbers[low] + numbers[high]
            if sum == target:
                return [low+1, high+1]
            elif sum < target:
                low += 1
            else:
                high -= 1
        return [-1, -1]


if __name__ == '__main__':
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert Solution().twoSum([2, 7, 11, 15], 18) == [2, 3]
    assert Solution().twoSum([2, 7, 11, 15], 12) == [-1, -1]
