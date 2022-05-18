/*
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

 
Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"

 
Constraints:
	1 <= s.length <= 1000
	s consists of lowercase English letters.

 
Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/
*/
#include <cassert>
#include <iostream>

class Solution {
public:
    string smallestSubsequence(string s) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.smallestSubsequence(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
