/*
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 
Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

 
Constraints:
	1 <= s.length <= 1000
	s consists only of lowercase English letters.


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    int longestPalindromeSubseq(string s) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.longestPalindromeSubseq(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
