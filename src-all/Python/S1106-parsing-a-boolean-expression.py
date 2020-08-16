"""
Return the result of evaluating a given boolean expression, represented as a string.

An expression can either be:

	&quot;t&quot;, evaluating to True;
	&quot;f&quot;, evaluating to False;
	&quot;!(expr)&quot;, evaluating to the logical NOT of the inner expression expr;
	&quot;&amp;(expr1,expr2,...)&quot;, evaluating to the logical AND of 2 or more inner expressions expr1, expr2, ...;
	&quot;|(expr1,expr2,...)&quot;, evaluating to the logical OR of 2 or more inner expressions expr1, expr2, ...

 
Example 1:
Input: expression = &quot;!(f)&quot;
Output: true

Example 2:
Input: expression = &quot;|(f,t)&quot;
Output: true

Example 3:
Input: expression = &quot;&amp;(t,f)&quot;
Output: false

Example 4:
Input: expression = &quot;|(&amp;(t,f,t),!(t))&quot;
Output: false

 
Constraints:
	1 <= expression.length <= 20000
	expression[i] consists of characters in {&#39;(&#39;, &#39;)&#39;, &#39;&amp;&#39;, &#39;|&#39;, &#39;!&#39;, &#39;t&#39;, &#39;f&#39;, &#39;,&#39;}.
	expression is a valid expression representing a boolean, as given in the description.


"""
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().parseBoolExpr(0) == 0

