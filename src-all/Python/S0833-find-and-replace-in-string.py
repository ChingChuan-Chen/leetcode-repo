"""
To some string S, we will perform some replacement operations that replace groups of letters with new ones (not necessarily the same size).

Each replacement operation has 3 parameters: a starting index i, a source word x and a target word y.  The rule is that if x starts at position i in the original string S, then we will replace that occurrence of x with y.  If not, we do nothing.

For example, if we have S = &quot;abcd&quot; and we have some replacement operation i = 2, x = &quot;cd&quot;, y = &quot;ffff&quot;, then because &quot;cd&quot; starts at position 2 in the original string S, we will replace it with &quot;ffff&quot;.

Using another example on S = &quot;abcd&quot;, if we have both the replacement operation i = 0, x = &quot;ab&quot;, y = &quot;eee&quot;, as well as another replacement operation i = 2, x = &quot;ec&quot;, y = &quot;ffff&quot;, this second operation does nothing because in the original string S[2] = &#39;c&#39;, which doesn&#39;t match x[0] = &#39;e&#39;.

All these operations occur simultaneously.  It&#39;s guaranteed that there won&#39;t be any overlap in replacement: for example, S = &quot;abc&quot;, indexes = [0, 1], sources = [&quot;ab&quot;,&quot;bc&quot;] is not a valid test case.

Example 1:
Input: S = &quot;abcd&quot;, indexes = [0,2], sources = [&quot;a&quot;,&quot;cd&quot;], targets = [&quot;eee&quot;,&quot;ffff&quot;]
Output: &quot;eeebffff&quot;
Explanation: &quot;a&quot; starts at index 0 in S, so it&#39;s replaced by &quot;eee&quot;.
&quot;cd&quot; starts at index 2 in S, so it&#39;s replaced by &quot;ffff&quot;.

Example 2:
Input: S = &quot;abcd&quot;, indexes = [0,2], sources = [&quot;ab&quot;,&quot;ec&quot;], targets = [&quot;eee&quot;,&quot;ffff&quot;]
Output: &quot;eeecd&quot;
Explanation: &quot;ab&quot; starts at index 0 in S, so it&#39;s replaced by &quot;eee&quot;. 
&quot;ec&quot; doesn&#39;t starts at index 2 in the original S, so we do nothing.

Notes:

	0 <= indexes.length = sources.length = targets.length <= 100
	0 < indexes[i] < S.length <= 1000
	All characters in given inputs are lowercase letters.

 

"""
from typing import List
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().findReplaceString(0) == 0

