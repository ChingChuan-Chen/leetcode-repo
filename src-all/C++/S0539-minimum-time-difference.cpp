/*
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 
Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

 
Constraints:
	2 <= timePoints.length <= 2 * 104
	timePoints[i] is in the format "HH:MM".


*/

class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

#include <cassert>
#include <iostream>

class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.findMinDifference(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
