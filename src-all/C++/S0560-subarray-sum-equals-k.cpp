/*
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

 
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

 
Constraints:
	1 <= nums.length <= 2 * 104
	-1000 <= nums[i] <= 1000
	-107 <= k <= 107


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.subarraySum(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
