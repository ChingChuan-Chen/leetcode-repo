"""
Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.

 
Example 1:
Input: s = &quot;HOW ARE YOU&quot;
Output: [&quot;HAY&quot;,&quot;ORO&quot;,&quot;WEU&quot;]
Explanation: Each word is printed vertically. 
 &quot;HAY&quot;
 &quot;ORO&quot;
 &quot;WEU&quot;

Example 2:
Input: s = &quot;TO BE OR NOT TO BE&quot;
Output: [&quot;TBONTB&quot;,&quot;OEROOE&quot;,&quot;   T&quot;]
Explanation: Trailing spaces is not allowed. 
&quot;TBONTB&quot;
&quot;OEROOE&quot;
&quot;   T&quot;

Example 3:
Input: s = &quot;CONTEST IS COMING&quot;
Output: [&quot;CIC&quot;,&quot;OSO&quot;,&quot;N M&quot;,&quot;T I&quot;,&quot;E N&quot;,&quot;S G&quot;,&quot;T&quot;]

 
Constraints:
	1 <= s.length <= 200
	s contains only upper case English letters.
	It&#39;s guaranteed that there is only one space between 2 words.

"""
from typing import List
class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().printVertically(0) == 0

