/*
Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

 
Constraints:
	1 <= ransomNote.length, magazine.length <= 105
	ransomNote and magazine consist of lowercase English letters.


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.canConstruct(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
