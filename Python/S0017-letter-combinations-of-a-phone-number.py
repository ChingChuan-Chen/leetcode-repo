"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations
that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

1: None, 2: abc, 3: def
4: ghi,  5: jkl, 6: mno
7: pqrs, 8: tuv, 9: wxyz

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digit_mapping = {"0": " ", "1": "", "2": "abc", "3": "def", "4": "ghi",
                         "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        res: List[str] = []
        def dfs(idx: int, path: str):
            if len(path) == len(digits):
                res.append(path)
                return
            for i in range(idx, len(digits)):
                for j in digit_mapping[digits[idx]]:
                    dfs(i+1, path+j)
        dfs(0, "")
        return res

        ## non-recursive solution
        # ans = [""]
        # for digit in digits:
        #     tmp = []
        #     for temp in ans:
        #         s = digit_mapping[digit]
        #         for i in s:
        #             tmp.append(temp + i)
        #     ans = tmp
        # return ans

if __name__ == '__main__':
    assert Solution().letterCombinations("") == []
    assert Solution().letterCombinations("1") == []
    assert Solution().letterCombinations("2") == ['a', 'b', 'c']
    assert Solution().letterCombinations("202") == ['a a', 'a b', 'a c', 'b a', 'b b', 'b c', 'c a', 'c b', 'c c']
    assert Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert Solution().letterCombinations("777") == ['ppp', 'ppq', 'ppr', 'pps', 'pqp', 'pqq', 'pqr', 'pqs',
                                                    'prp', 'prq', 'prr', 'prs', 'psp', 'psq', 'psr', 'pss',
                                                    'qpp', 'qpq', 'qpr', 'qps', 'qqp', 'qqq', 'qqr', 'qqs',
                                                    'qrp', 'qrq', 'qrr', 'qrs', 'qsp', 'qsq', 'qsr', 'qss',
                                                    'rpp', 'rpq', 'rpr', 'rps', 'rqp', 'rqq', 'rqr', 'rqs',
                                                    'rrp', 'rrq', 'rrr', 'rrs', 'rsp', 'rsq', 'rsr', 'rss',
                                                    'spp', 'spq', 'spr', 'sps', 'sqp', 'sqq', 'sqr', 'sqs',
                                                    'srp', 'srq', 'srr', 'srs', 'ssp', 'ssq', 'ssr', 'sss']
