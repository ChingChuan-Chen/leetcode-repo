"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
from typing import List
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        res: List[List[int]] = []
        def dfs(counter, path: List[int]):
            if len(path) == len(nums):
                res.append(path)
                return
            for x in counter:
                if counter[x]:
                    counter[x] -= 1
                    dfs(counter, path + [x])
                    counter[x] += 1

        dfs(Counter(nums), [])
        return res


if __name__ == '__main__':
    assert Solution().permuteUnique([1, 2]) == [[1, 2], [2, 1]]
    assert Solution().permuteUnique([2, 2]) == [[2, 2]]
    assert Solution().permuteUnique([1, 1, 2]) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    assert Solution().permuteUnique([1, 1, 2, 2]) == [[1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1],
                                                      [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]]
