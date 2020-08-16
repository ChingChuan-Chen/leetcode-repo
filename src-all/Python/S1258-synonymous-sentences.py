"""
Given a list of pairs of equivalent words synonyms and a sentence text, Return all possible synonymous sentences sorted lexicographically.
 
Example 1:
Input:
synonyms = [[&quot;happy&quot;,&quot;joy&quot;],[&quot;sad&quot;,&quot;sorrow&quot;],[&quot;joy&quot;,&quot;cheerful&quot;]],
text = &quot;I am happy today but was sad yesterday&quot;
Output:
[&quot;I am cheerful today but was sad yesterday&quot;,
<U+200B><U+200B><U+200B><U+200B><U+200B><U+200B><U+200B>&quot;I am cheerful today but was sorrow yesterday&quot;,
&quot;I am happy today but was sad yesterday&quot;,
&quot;I am happy today but was sorrow yesterday&quot;,
&quot;I am joy today but was sad yesterday&quot;,
&quot;I am joy today but was sorrow yesterday&quot;]

 
Constraints:
	0 <= synonyms.length <= 10
	synonyms[i].length == 2
	synonyms[i][0] != synonyms[i][1]
	All words consist of at most 10 English letters only.
	text is a single space separated sentence of at most 10 words.


"""
from typing import List
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().generateSentences(0) == 0

