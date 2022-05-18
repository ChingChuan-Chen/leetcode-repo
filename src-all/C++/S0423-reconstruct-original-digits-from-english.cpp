/*
Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

 
Example 1:
Input: s = "owoztneoer"
Output: "012"
Example 2:
Input: s = "fviefuro"
Output: "45"

 
Constraints:
	1 <= s.length <= 105
	s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
	s is guaranteed to be valid.


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    string originalDigits(string s) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.originalDigits(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
