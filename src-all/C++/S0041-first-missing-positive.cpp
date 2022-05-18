/*
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 
Example 1:
Input: nums = [1,2,0]
Output: 3
Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Example 3:
Input: nums = [7,8,9,11,12]
Output: 1

 
Constraints:
	1 <= nums.length <= 5 * 105
	-231 <= nums[i] <= 231 - 1


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.firstMissingPositive(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
