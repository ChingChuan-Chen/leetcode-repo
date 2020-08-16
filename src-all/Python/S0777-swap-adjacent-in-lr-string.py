"""
In a string composed of &#39;L&#39;, &#39;R&#39;, and &#39;X&#39; characters, like &quot;RXXLRXRXL&quot;, a move consists of either replacing one occurrence of &quot;XL&quot; with &quot;LX&quot;, or replacing one occurrence of &quot;RX&quot; with &quot;XR&quot;. Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

Example:

Input: start = &quot;RXXLRXRXL&quot;, end = &quot;XRLXXRRLX&quot;
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

 
Constraints:
	1 <= len(start) == len(end) <= 10000.
	Both start and end will only consist of characters in {&#39;L&#39;, &#39;R&#39;, &#39;X&#39;}.


"""
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().canTransform(0) == 0

