/*
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.

 
Example 1:
Input: points = [[1,1],[2,3],[3,2]]
Output: true
Example 2:
Input: points = [[1,1],[2,2],[3,3]]
Output: false

 
Constraints:
	points.length == 3
	points[i].length == 2
	0 <= xi, yi <= 100


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    bool isBoomerang(vector<vector<int>>& points) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.isBoomerang(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
