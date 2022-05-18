/*
Given a string s, return the last substring of s in lexicographical order.

 
Example 1:
Input: s = "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".

Example 2:
Input: s = "leetcode"
Output: "tcode"

 
Constraints:
	1 <= s.length <= 4 * 105
	s contains only lowercase English letters.


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    string lastSubstring(string s) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.lastSubstring(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
