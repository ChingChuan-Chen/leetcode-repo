"""
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

Example:

Input:
[
  &quot;0010&quot;,
  &quot;0110&quot;,
  &quot;0100&quot;
]
and x = 0, y = 2

Output: 6


"""
from typing import List
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().minArea(0) == 0

