/*
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [A, B] where:

	A and B are No-Zero integers.
	A + B = n

The test cases are generated so that there is at least one valid solution. If there are many valid solutions you can return any of them.

 
Example 1:
Input: n = 2
Output: [1,1]
Explanation: A = 1, B = 1. A + B = n and both A and B do not contain any 0 in their decimal representation.

Example 2:
Input: n = 11
Output: [2,9]

 
Constraints:
	2 <= n <= 104


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.getNoZeroIntegers(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
