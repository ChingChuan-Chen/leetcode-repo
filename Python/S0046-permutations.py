"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from typing import List
from collections import Counter
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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

        ## non-recursive method
        # nums_set = set(nums)
        # ans = [[]]
        # for _ in range(len(nums)):
        #     tmp = []
        #     for temp in ans:
        #         remain_set = nums_set - set(temp)
        #         for x in remain_set:
        #             tmp.append(temp + [x])
        #     ans = tmp
        # return ans


if __name__ == '__main__':
    assert Solution().permute([]) == []
    assert Solution().permute([1]) == [[1]]
    assert Solution().permute([1, 2]) == [[1, 2], [2, 1]]
    assert Solution().permute([1, 2, 3]) == [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
