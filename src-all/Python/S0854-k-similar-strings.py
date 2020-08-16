"""
Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly K times so that the resulting string equals B.

Given two anagrams A and B, return the smallest K for which A and B are K-similar.

Example 1:
Input: A = &quot;ab&quot;, B = &quot;ba&quot;
Output: 1

Example 2:
Input: A = &quot;abc&quot;, B = &quot;bca&quot;
Output: 2

Example 3:
Input: A = &quot;abac&quot;, B = &quot;baca&quot;
Output: 2

Example 4:
Input: A = &quot;aabc&quot;, B = &quot;abca&quot;
Output: 2

Note:
	1 <= A.length == B.length <= 20
	A and B contain only lowercase letters from the set {&#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;, &#39;e&#39;, &#39;f&#39;}


"""
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().kSimilarity(0) == 0

