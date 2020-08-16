"""
You are given two strings s1 and s2 of equal length consisting of letters &quot;x&quot; and &quot;y&quot; only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

 
Example 1:
Input: s1 = &quot;xx&quot;, s2 = &quot;yy&quot;
Output: 1
Explanation: 
Swap s1[0] and s2[1], s1 = &quot;yx&quot;, s2 = &quot;yx&quot;.

Example 2: 

Input: s1 = &quot;xy&quot;, s2 = &quot;yx&quot;
Output: 2
Explanation: 
Swap s1[0] and s2[0], s1 = &quot;yy&quot;, s2 = &quot;xx&quot;.
Swap s1[0] and s2[1], s1 = &quot;xy&quot;, s2 = &quot;xy&quot;.
Note that you can&#39;t swap s1[0] and s1[1] to make s1 equal to &quot;yx&quot;, cause we can only swap chars in different strings.

Example 3:
Input: s1 = &quot;xx&quot;, s2 = &quot;xy&quot;
Output: -1

Example 4:
Input: s1 = &quot;xxyyxyxyxx&quot;, s2 = &quot;xyyxyxxxyx&quot;
Output: 4

 
Constraints:
	1 <= s1.length, s2.length <= 1000
	s1, s2 only contain &#39;x&#39; or &#39;y&#39;.


"""
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().minimumSwap(0) == 0

