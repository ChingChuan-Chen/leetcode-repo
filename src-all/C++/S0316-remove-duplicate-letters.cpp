/*
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 
Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"

 
Constraints:
	1 <= s.length <= 104
	s consists of lowercase English letters.

 
Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

*/
#include <cassert>
#include <iostream>

class Solution {
public:
    string removeDuplicateLetters(string s) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.removeDuplicateLetters(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
