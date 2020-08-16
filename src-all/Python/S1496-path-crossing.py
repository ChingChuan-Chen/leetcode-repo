"""
Given a string path, where path[i] = &#39;N&#39;, &#39;S&#39;, &#39;E&#39; or &#39;W&#39;, each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return True if the path crosses itself at any point, that is, if at any time you are on a location you&#39;ve previously visited. Return False otherwise.

 
Example 1:
Input: path = &quot;NES&quot;
Output: false 
Explanation: Notice that the path doesn&#39;t cross any point more than once.

Example 2:
Input: path = &quot;NESWW&quot;
Output: true
Explanation: Notice that the path visits the origin twice.

 
Constraints:
	1 <= path.length <= 10^4
	path will only consist of characters in {&#39;N&#39;, &#39;S&#39;, &#39;E&#39;, &#39;W}


"""
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().isPathCrossing(0) == 0

