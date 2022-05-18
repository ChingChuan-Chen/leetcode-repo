/*
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 
Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:
Input: s = "a"
Output: [["a"]]

 
Constraints:
	1 <= s.length <= 16
	s contains only lowercase English letters.


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    vector<vector<string>> partition(string s) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.partition(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
