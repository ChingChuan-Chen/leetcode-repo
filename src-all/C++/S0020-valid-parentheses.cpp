/*
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

	Open brackets must be closed by the same type of brackets.
	Open brackets must be closed in the correct order.

 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

 
Constraints:
	1 <= s.length <= 104
	s consists of parentheses only '()[]{}'.


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    bool isValid(string s) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.isValid(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
