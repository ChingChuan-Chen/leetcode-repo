/*
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 
Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

 
Constraints:
	1 <= s.length <= 105
	s consists of lowercase English letters.


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    bool validPalindrome(string s) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.validPalindrome(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
