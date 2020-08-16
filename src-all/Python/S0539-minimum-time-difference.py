"""
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list. 

Example 1:
Input: ["23:59","00:00"]
Output: 1

Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.


"""

class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().findMinDifference(0) == 0

