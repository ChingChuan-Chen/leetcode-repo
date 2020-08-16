"""
A string is a valid parentheses string (denoted VPS) if and only if it consists of &quot;(&quot; and &quot;)&quot; characters only, and:

	It is the empty string, or
	It can be written as AB (A concatenated with B), where A and B are VPS&#39;s, or
	It can be written as (A), where A is a VPS.

We can similarly define the nesting depth depth(S) of any VPS S as follows:

	depth(&quot;&quot;) = 0
	depth(A + B) = max(depth(A), depth(B)), where A and B are VPS&#39;s
	depth(&quot;(&quot; + A + &quot;)&quot;) = 1 + depth(A), where A is a VPS.

For example,  &quot;&quot;, &quot;()()&quot;, and &quot;()(()())&quot; are VPS&#39;s (with nesting depths 0, 1, and 2), and &quot;)(&quot; and &quot;(()&quot; are not VPS&#39;s.

 

Given a VPS seq, split it into two disjoint subsequences A and B, such that A and B are VPS&#39;s (and A.length + B.length = seq.length).

Now choose any such A and B such that max(depth(A), depth(B)) is the minimum possible value.

Return an answer array (of length seq.length) that encodes such a choice of A and B:  answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.  Note that even though multiple answers may exist, you may return any of them.

 
Example 1:
Input: seq = &quot;(()())&quot;
Output: [0,1,1,1,1,0]

Example 2:
Input: seq = &quot;()(())()&quot;
Output: [0,0,0,1,1,0,1,1]

 
Constraints:
	1 <= seq.size <= 10000


"""
from typing import List
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        
        pass


if __name__ == '__main__':
    assert Solution().maxDepthAfterSplit(0) == 0

