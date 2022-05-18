/*
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

 
Example 1:
Input: n = 1
Output: true

Example 2:
Input: n = 10
Output: false

 
Constraints:
	1 <= n <= 109


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    bool reorderedPowerOf2(int n) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.reorderedPowerOf2(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
