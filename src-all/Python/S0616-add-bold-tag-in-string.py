"""
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:
Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"

 

Example 2:
Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"

 

Constraints:
	The given dict won&#39;t contain duplicates, and its length won&#39;t exceed 100.
	All the strings in input have length in range [1, 1000].

Note: This question is the same as 758: https://leetcode.com/problems/bold-words-in-string/

"""
from typing import List
class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().addBoldTag(0) == 0

