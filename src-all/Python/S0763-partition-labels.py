"""
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:
Input: S = &quot;ababcbacadefegdehijhklij&quot;
Output: [9,7,8]
Explanation:
The partition is &quot;ababcbaca&quot;, &quot;defegde&quot;, &quot;hijhklij&quot;.
This is a partition so that each letter appears in at most one part.
A partition like &quot;ababcbacadefegde&quot;, &quot;hijhklij&quot; is incorrect, because it splits S into less parts.

 

Note:
	S will have length in range [1, 500].
	S will consist of lowercase English letters (&#39;a&#39; to &#39;z&#39;) only.

 

"""
from typing import List
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        pass


if __name__ == '__main__':
    assert Solution().partitionLabels(0) == 0

