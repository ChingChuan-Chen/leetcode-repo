"""
HTML entity parser is the parser that takes HTML code as input and replace all the entities of the special characters by the characters itself.

The special characters and their entities for HTML are:

	Quotation Mark: the entity is &amp;quot; and symbol character is &quot;.
	Single Quote Mark: the entity is &amp;apos; and symbol character is &#39;.
	Ampersand: the entity is &amp;amp; and symbol character is &amp;.
	Greater Than Sign: the entity is &amp;gt; and symbol character is >.
	Less Than Sign: the entity is &amp;lt; and symbol character is <.
	Slash: the entity is &amp;frasl; and symbol character is /.

Given the input text string to the HTML parser, you have to implement the entity parser.

Return the text after replacing the entities by the special characters.

 
Example 1:
Input: text = &quot;&amp;amp; is an HTML entity but &amp;ambassador; is not.&quot;
Output: &quot;&amp; is an HTML entity but &amp;ambassador; is not.&quot;
Explanation: The parser will replace the &amp;amp; entity by &amp;

Example 2:
Input: text = &quot;and I quote: &amp;quot;...&amp;quot;&quot;
Output: &quot;and I quote: \&quot;...\&quot;&quot;

Example 3:
Input: text = &quot;Stay home! Practice on Leetcode :)&quot;
Output: &quot;Stay home! Practice on Leetcode :)&quot;

Example 4:
Input: text = &quot;x &amp;gt; y &amp;amp;&amp;amp; x &amp;lt; y is always false&quot;
Output: &quot;x > y &amp;&amp; x < y is always false&quot;

Example 5:
Input: text = &quot;leetcode.com&amp;frasl;problemset&amp;frasl;all&quot;
Output: &quot;leetcode.com/problemset/all&quot;

 
Constraints:
	1 <= text.length <= 10^5
	The string may contain any possible characters out of all the 256 ASCII characters.


"""
class Solution:
    def entityParser(self, text: str) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().entityParser(0) == 0

