"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:
Input: A = &quot;this apple is sweet&quot;, B = &quot;this apple is sour&quot;
Output: [&quot;sweet&quot;,&quot;sour&quot;]

Example 2:
Input: A = &quot;apple apple&quot;, B = &quot;banana&quot;
Output: [&quot;banana&quot;]

 

Note:
	0 <= A.length <= 200
	0 <= B.length <= 200
	A and B both contain only spaces and lowercase letters.


"""
from typing import List
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().uncommonFromSentences(0) == 0

