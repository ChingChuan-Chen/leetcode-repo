"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        
        res: List[List[int]] = []
        def dfs(idx, path: List[int]):
            res.append(path)
            for i in range(idx, len(nums)):
                dfs(i + 1, path + [nums[i]])
        dfs(0, [])
        return res


if __name__ == '__main__':
    assert Solution().subsets([]) == [[]]
    assert Solution().subsets([1]) == [[], [1]]
    assert Solution().subsets([1, 2]) == [[], [1], [1, 2], [2]]
    assert Solution().subsets([1, 2, 3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
