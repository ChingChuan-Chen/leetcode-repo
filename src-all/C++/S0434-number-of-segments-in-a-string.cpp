/*
Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.

 
Example 1:
Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

Example 2:
Input: s = "Hello"
Output: 1

 
Constraints:
	0 <= s.length <= 300
	s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&amp;*()_+-=',.:".
	The only space character in s is ' '.


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    int countSegments(string s) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.countSegments(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
