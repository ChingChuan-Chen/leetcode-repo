"""
Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: &quot;a==b&quot; or &quot;a!=b&quot;.  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

 

Example 1:
Input: [&quot;a==b&quot;,&quot;b!=a&quot;]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.

Example 2:
Input: [&quot;b==a&quot;,&quot;a==b&quot;]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

Example 3:
Input: [&quot;a==b&quot;,&quot;b==c&quot;,&quot;a==c&quot;]
Output: true

Example 4:
Input: [&quot;a==b&quot;,&quot;b!=c&quot;,&quot;c==a&quot;]
Output: false

Example 5:
Input: [&quot;c==c&quot;,&quot;b==d&quot;,&quot;x!=z&quot;]
Output: true

 

Note:
	1 <= equations.length <= 500
	equations[i].length == 4
	equations[i][0] and equations[i][3] are lowercase letters
	equations[i][1] is either &#39;=&#39; or &#39;!&#39;
	equations[i][2] is &#39;=&#39;


"""
from typing import List
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().equationsPossible(0) == 0

