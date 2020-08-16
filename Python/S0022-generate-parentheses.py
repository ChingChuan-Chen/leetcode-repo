"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        res: List[str] = []
        def dfs(left: int, right: int, path: str):
            if left == n and right == n:
                res.append(path)
                return
            if left == 0:
                dfs(left + 1, right, path + "(")
            elif n > left >= right:
                dfs(left + 1, right, path + "(")
                dfs(left, right + 1, path + ")")
            elif right < left == n:
                dfs(left, right + 1, path + ")")
        dfs(0, 0, "")
        return res

        ## non-recursive solution
        # ans = {"": [0, 0]}
        # for _ in range(n*2):
        #     tmp = {}
        #     for k, v in ans.items():
        #         if v[0] == 0:
        #             tmp[k + "("] = [v[0] + 1, v[1]]
        #         elif v[1] <= v[0] < n:
        #             tmp[k + "("] = [v[0] + 1, v[1]]
        #             tmp[k + ")"] = [v[0], v[1] + 1]
        #         elif v[1] < v[0] == n:
        #             tmp[k +")"] = [v[0], v[1]+1]
        #     ans = tmp
        # return list(ans.keys())

if __name__ == '__main__':
    assert Solution().generateParenthesis(0) == []
    assert Solution().generateParenthesis(1) == ["()"]
    assert Solution().generateParenthesis(2) == ["(())", "()()"]
    assert Solution().generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert Solution().generateParenthesis(4) == ['(((())))', '((()()))', '((())())', '((()))()',
                                                 '(()(()))', '(()()())', '(()())()', '(())(())',
                                                 '(())()()', '()((()))', '()(()())', '()(())()',
                                                 '()()(())', '()()()()']
