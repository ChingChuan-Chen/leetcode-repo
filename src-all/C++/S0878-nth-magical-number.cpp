/*
A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.

 
Example 1:
Input: n = 1, a = 2, b = 3
Output: 2

Example 2:
Input: n = 4, a = 2, b = 3
Output: 6

 
Constraints:
	1 <= n <= 109
	2 <= a, b <= 4 * 104


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    int nthMagicalNumber(int n, int a, int b) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.nthMagicalNumber(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
