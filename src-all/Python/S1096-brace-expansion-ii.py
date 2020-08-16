"""
Under a grammar given below, strings can represent a set of lowercase words.  Let&#39;s use R(expr) to denote the set of words the expression represents.

Grammar can best be understood through simple examples:

	Single letters represent a singleton set containing that word.
	
		R(&quot;a&quot;) = {&quot;a&quot;}
		R(&quot;w&quot;) = {&quot;w&quot;}
	
	
	When we take a comma delimited list of 2 or more expressions, we take the union of possibilities.
	
		R(&quot;{a,b,c}&quot;) = {&quot;a&quot;,&quot;b&quot;,&quot;c&quot;}
		R(&quot;{{a,b},{b,c}}&quot;) = {&quot;a&quot;,&quot;b&quot;,&quot;c&quot;} (notice the final set only contains each word at most once)
	
	
	When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
	
		R(&quot;{a,b}{c,d}&quot;) = {&quot;ac&quot;,&quot;ad&quot;,&quot;bc&quot;,&quot;bd&quot;}
		R(&quot;a{b,c}{d,e}f{g,h}&quot;) = {&quot;abdfg&quot;, &quot;abdfh&quot;, &quot;abefg&quot;, &quot;abefh&quot;, &quot;acdfg&quot;, &quot;acdfh&quot;, &quot;acefg&quot;, &quot;acefh&quot;}
	
	

Formally, the 3 rules for our grammar:

	For every lowercase letter x, we have R(x) = {x}
	For expressions e_1, e_2, ... , e_k with k >= 2, we have R({e_1,e_2,...}) = R(e_1) &cup; R(e_2) &cup; ...
	For expressions e_1 and e_2, we have R(e_1 + e_2) = {a + b for (a, b) in R(e_1) &times; R(e_2)}, where + denotes concatenation, and &times; denotes the cartesian product.

Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.

 

Example 1:
Input: &quot;{a,b}{c,{d,e}}&quot;
Output: [&quot;ac&quot;,&quot;ad&quot;,&quot;ae&quot;,&quot;bc&quot;,&quot;bd&quot;,&quot;be&quot;]

Example 2:
Input: &quot;{{a,z},a{b,c},{ab,z}}&quot;
Output: [&quot;a&quot;,&quot;ab&quot;,&quot;ac&quot;,&quot;z&quot;]
Explanation: Each distinct word is written only once in the final answer.

 

Constraints:
	1 <= expression.length <= 60
	expression[i] consists of &#39;{&#39;, &#39;}&#39;, &#39;,&#39;or lowercase English letters.
	The given expression represents a set of words based on the grammar given in the description.


"""
from typing import List
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().braceExpansionII(0) == 0

