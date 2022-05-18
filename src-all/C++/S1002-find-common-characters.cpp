/*
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 
Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

 
Constraints:
	1 <= words.length <= 100
	1 <= words[i].length <= 100
	words[i] consists of lowercase English letters.


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.commonChars(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
