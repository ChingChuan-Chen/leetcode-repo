"""
Given the string croakOfFrogs, which represents a combination of the string &quot;croak&quot; from different frogs, that is, multiple frogs can croak at the same time, so multiple &ldquo;croak&rdquo; are mixed. Return the minimum number of different frogs to finish all the croak in the given string.

A valid &quot;croak&quot; means a frog is printing 5 letters &lsquo;c&rsquo;, &rsquo;r&rsquo;, &rsquo;o&rsquo;, &rsquo;a&rsquo;, &rsquo;k&rsquo; sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of valid &quot;croak&quot; return -1.

 
Example 1:
Input: croakOfFrogs = &quot;croakcroak&quot;
Output: 1 
Explanation: One frog yelling &quot;croak&quot; twice.

Example 2:
Input: croakOfFrogs = &quot;crcoakroak&quot;
Output: 2 
Explanation: The minimum number of frogs is two. 
The first frog could yell &quot;crcoakroak&quot;.
The second frog could yell later &quot;crcoakroak&quot;.

Example 3:
Input: croakOfFrogs = &quot;croakcrook&quot;
Output: -1
Explanation: The given string is an invalid combination of &quot;croak&quot; from different frogs.

Example 4:
Input: croakOfFrogs = &quot;croakcroa&quot;
Output: -1

 
Constraints:
	1 <= croakOfFrogs.length <= 10^5
	All characters in the string are: &#39;c&#39;, &#39;r&#39;, &#39;o&#39;, &#39;a&#39; or &#39;k&#39;.


"""
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().minNumberOfFrogs(0) == 0

