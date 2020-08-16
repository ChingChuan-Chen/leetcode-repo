"""
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as &quot;\\&quot;.)

Return the number of regions.

 

Example 1:
Input:
[
  &quot; /&quot;,
  &quot;/ &quot;
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:
Input:
[
  &quot; /&quot;,
  &quot;  &quot;
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:
Input:
[
  &quot;\\/&quot;,
  &quot;/\\&quot;
]
Output: 4
Explanation: (Recall that because \ characters are escaped, &quot;\\/&quot; refers to \/, and &quot;/\\&quot; refers to /\.)
The 2x2 grid is as follows:

Example 4:
Input:
[
  &quot;/\\&quot;,
  &quot;\\/&quot;
]
Output: 5
Explanation: (Recall that because \ characters are escaped, &quot;/\\&quot; refers to /\, and &quot;\\/&quot; refers to \/.)
The 2x2 grid is as follows:

Example 5:
Input:
[
  &quot;//&quot;,
  &quot;/ &quot;
]
Output: 3
Explanation: The 2x2 grid is as follows:

 

Note:
	1 <= grid.length == grid[0].length <= 30
	grid[i][j] is either &#39;/&#39;, &#39;\&#39;, or &#39; &#39;.


"""
from typing import List
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().regionsBySlashes(0) == 0

