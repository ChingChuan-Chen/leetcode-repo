/*
Given an integer array of size n, find all elements that appear more than &lfloor; n/3 &rfloor; times.

 
Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]

 
Constraints:
	1 <= nums.length <= 5 * 104
	-109 <= nums[i] <= 109

 
Follow up: Could you solve the problem in linear time and in O(1) space?

*/
#include <cassert>
#include <iostream>

class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.majorityElement(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
