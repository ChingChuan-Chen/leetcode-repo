"""
Given a 2D board containing &#39;X&#39; and &#39;O&#39; (the letter O), capture all regions surrounded by &#39;X&#39;.

A region is captured by flipping all &#39;O&#39;s into &#39;X&#39;s in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn&rsquo;t be on the border, which means that any &#39;O&#39; on the border of the board are not flipped to &#39;X&#39;. Any &#39;O&#39; that is not on the border and it is not connected to an &#39;O&#39; on the border will be flipped to &#39;X&#39;. Two cells are connected if they are adjacent cells connected horizontally or vertically.

"""
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        pass


if __name__ == '__main__':
    assert Solution().solve(0) == 0

