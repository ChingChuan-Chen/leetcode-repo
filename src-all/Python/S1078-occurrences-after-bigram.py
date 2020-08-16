"""
Given words first and second, consider occurrences in some text of the form &quot;first second third&quot;, where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add &quot;third&quot; to the answer, and return the answer.

 

Example 1:
Input: text = &quot;alice is a good girl she is a good student&quot;, first = &quot;a&quot;, second = &quot;good&quot;
Output: [&quot;girl&quot;,&quot;student&quot;]

Example 2:
Input: text = &quot;we will we will rock you&quot;, first = &quot;we&quot;, second = &quot;will&quot;
Output: [&quot;we&quot;,&quot;rock&quot;]

 

Note:
	1 <= text.length <= 1000
	text consists of space separated words, where each word consists of lowercase English letters.
	1 <= first.length, second.length <= 10
	first and second consist of lowercase English letters.


"""
from typing import List
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().findOcurrences(0) == 0

