"""
Given an equation, represented by words on left side and the result on right side.

You need to check if the equation is solvable under the following rules:

	Each character is decoded as one digit (0 - 9).
	Every pair of different characters they must map to different digits.
	Each words[i] and result are decoded as one number without leading zeros.
	Sum of numbers on left side (words) will equal to the number on right side (result). 

Return True if the equation is solvable otherwise return False.

 
Example 1:
Input: words = ["SEND","MORE"], result = "MONEY"
Output: true
Explanation: Map &#39;S&#39;-> 9, &#39;E&#39;->5, &#39;N&#39;->6, &#39;D&#39;->7, &#39;M&#39;->1, &#39;O&#39;->0, &#39;R&#39;->8, &#39;Y&#39;->&#39;2&#39;
Such that: "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652

Example 2:
Input: words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
Output: true
Explanation: Map &#39;S&#39;-> 6, &#39;I&#39;->5, &#39;X&#39;->0, &#39;E&#39;->8, &#39;V&#39;->7, &#39;N&#39;->2, &#39;T&#39;->1, &#39;W&#39;->&#39;3&#39;, &#39;Y&#39;->4
Such that: "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214

Example 3:
Input: words = ["THIS","IS","TOO"], result = "FUNNY"
Output: true

Example 4:
Input: words = ["LEET","CODE"], result = "POINT"
Output: false

 
Constraints:
	2 <= words.length <= 5
	1 <= words[i].length, result.length <= 7
	words[i], result contains only upper case English letters.
	Number of different characters used on the expression is at most 10.


"""
from typing import List
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().isSolvable(0) == 0

