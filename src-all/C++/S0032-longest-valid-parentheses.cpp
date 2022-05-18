/*
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 
Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

 
Constraints:
	0 <= s.length <= 3 * 104
	s[i] is '(', or ')'.


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    int longestValidParentheses(string s) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.longestValidParentheses(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
