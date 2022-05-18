/*
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 
Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:
Input: arr = [1,1]
Output: 1

 
Constraints:
	1 <= arr.length <= 104
	0 <= arr[i] <= 105


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.findSpecialInteger(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
