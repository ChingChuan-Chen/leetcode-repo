/*
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

	Any left parenthesis '(' must have a corresponding right parenthesis ')'.
	Any right parenthesis ')' must have a corresponding left parenthesis '('.
	Left parenthesis '(' must go before the corresponding right parenthesis ')'.
	'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

 
Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "(*)"
Output: true
Example 3:
Input: s = "(*))"
Output: true

 
Constraints:
	1 <= s.length <= 100
	s[i] is '(', ')' or '*'.


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    bool checkValidString(string s) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.checkValidString(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
