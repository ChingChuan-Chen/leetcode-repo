/*
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

 
Example 1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5

 
Constraints:
	1 <= nums1.length, nums2.length <= 1000
	0 <= nums1[i], nums2[i] <= 100


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.findLength(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
