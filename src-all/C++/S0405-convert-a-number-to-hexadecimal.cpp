/*
Given an integer num, return a string representing its hexadecimal representation. For negative integers, two&rsquo;s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.

 
Example 1:
Input: num = 26
Output: "1a"
Example 2:
Input: num = -1
Output: "ffffffff"

 
Constraints:
	-231 <= num <= 231 - 1


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    string toHex(int num) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.toHex(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
