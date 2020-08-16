"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:
Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4

Example 2:
Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

"""

class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().maxPoints(0) == 0

