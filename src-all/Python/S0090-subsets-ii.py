"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]


"""
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        res: List[List[int]] = []
        nums.sort()
        def dfs(idx, path: List[int]):
            res.append(path)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                dfs(i + 1, path + [nums[i]])
        dfs(0, [])
        return res


if __name__ == '__main__':
    assert Solution().subsetsWithDup([]) == []
    assert Solution().subsetsWithDup([1]) == [[], [1]]
    assert Solution().subsetsWithDup([1, 2]) == [[], [1], [1, 2], [2]]
    assert Solution().subsetsWithDup([1, 2, 2]) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    assert Solution().subsetsWithDup([1, 1, 2, 2]) == [[], [1], [1, 1], [1, 1, 2], [1, 1, 2, 2],
                                                       [1, 2], [1, 2, 2], [2], [2, 2]]
assert Solution().subsetsWithDup([2, 1, 2])