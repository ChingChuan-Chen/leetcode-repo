/*
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

 
Example 1:
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Example 2:
Input: words = ["cat","dog","catdog"]
Output: ["catdog"]

 
Constraints:
	1 <= words.length <= 104
	0 <= words[i].length <= 30
	words[i] consists of only lowercase English letters.
	0 <= sum(words[i].length) <= 105


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.findAllConcatenatedWordsInADict(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
