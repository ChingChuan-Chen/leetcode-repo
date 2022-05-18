/*
Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

 
Example 1:
Input: s = "banana"
Output: "ana"
Example 2:
Input: s = "abcd"
Output: ""

 
Constraints:
	2 <= s.length <= 3 * 104
	s consists of lowercase English letters.


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    string longestDupSubstring(string s) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.longestDupSubstring(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
