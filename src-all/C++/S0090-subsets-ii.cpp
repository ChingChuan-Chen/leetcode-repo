/*
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 
Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:
Input: nums = [0]
Output: [[],[0]]

 
Constraints:
	1 <= nums.length <= 10
	-10 <= nums[i] <= 10


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.subsetsWithDup(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
