"""
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 
Example 1:
Input: name = &quot;alex&quot;, typed = &quot;aaleex&quot;
Output: true
Explanation: &#39;a&#39; and &#39;e&#39; in &#39;alex&#39; were long pressed.

Example 2:
Input: name = &quot;saeed&quot;, typed = &quot;ssaaedd&quot;
Output: false
Explanation: &#39;e&#39; must have been pressed twice, but it wasn&#39;t in the typed output.

Example 3:
Input: name = &quot;leelee&quot;, typed = &quot;lleeelee&quot;
Output: true

Example 4:
Input: name = &quot;laiden&quot;, typed = &quot;laiden&quot;
Output: true
Explanation: It&#39;s not necessary to long press any character.

 
Constraints:
	1 <= name.length <= 1000
	1 <= typed.length <= 1000
	The characters of name and typed are lowercase letters.


"""
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().isLongPressedName(0) == 0

