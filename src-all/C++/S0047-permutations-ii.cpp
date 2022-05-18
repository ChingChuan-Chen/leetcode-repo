/*
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 
Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

 
Constraints:
	1 <= nums.length <= 8
	-10 <= nums[i] <= 10


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.permuteUnique(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
