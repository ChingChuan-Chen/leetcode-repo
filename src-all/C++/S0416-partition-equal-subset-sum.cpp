/*
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 
Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

 
Constraints:
	1 <= nums.length <= 200
	1 <= nums[i] <= 100


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.canPartition(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
