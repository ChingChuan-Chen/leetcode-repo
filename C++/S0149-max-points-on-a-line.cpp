/*
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 
Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

 
Constraints:
	1 <= points.length <= 300
	points[i].length == 2
	-104 <= xi, yi <= 104
	All the points are unique.


*/

class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

#include <cassert>
#include <iostream>

class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.maxPoints(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
