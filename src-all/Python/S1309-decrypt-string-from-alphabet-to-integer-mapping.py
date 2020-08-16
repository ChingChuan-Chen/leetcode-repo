"""
Given a string s formed by digits (&#39;0&#39; - &#39;9&#39;) and &#39;#&#39; . We want to map s to English lowercase characters as follows:

	Characters (&#39;a&#39; to &#39;i&#39;) are represented by (&#39;1&#39; to &#39;9&#39;) respectively.
	Characters (&#39;j&#39; to &#39;z&#39;) are represented by (&#39;10#&#39; to &#39;26#&#39;) respectively. 

Return the string formed after mapping.

It&#39;s guaranteed that a unique mapping will always exist.

 
Example 1:
Input: s = &quot;10#11#12&quot;
Output: &quot;jkab&quot;
Explanation: &quot;j&quot; -> &quot;10#&quot; , &quot;k&quot; -> &quot;11#&quot; , &quot;a&quot; -> &quot;1&quot; , &quot;b&quot; -> &quot;2&quot;.

Example 2:
Input: s = &quot;1326#&quot;
Output: &quot;acz&quot;

Example 3:
Input: s = &quot;25#&quot;
Output: &quot;y&quot;

Example 4:
Input: s = &quot;12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#&quot;
Output: &quot;abcdefghijklmnopqrstuvwxyz&quot;

 
Constraints:
	1 <= s.length <= 1000
	s[i] only contains digits letters (&#39;0&#39;-&#39;9&#39;) and &#39;#&#39; letter.
	s will be valid string such that mapping is always possible.

"""
class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().freqAlphabets(0) == 0

