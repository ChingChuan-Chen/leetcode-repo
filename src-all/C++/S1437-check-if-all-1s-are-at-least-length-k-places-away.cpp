/*
Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

 
Example 1:
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.

Example 2:
Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.

 
Constraints:
	1 <= nums.length <= 105
	0 <= k <= nums.length
	nums[i] is 0 or 1


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.kLengthApart(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
