"""
A string S represents a list of words.

Each letter in the word has 1 or more options.  If there is one option, the letter is represented as is.  If there is more than one option, then curly braces delimit the options.  For example, &quot;{a,b,c}&quot; represents options [&quot;a&quot;, &quot;b&quot;, &quot;c&quot;].

For example, &quot;{a,b,c}d{e,f}&quot; represents the list [&quot;ade&quot;, &quot;adf&quot;, &quot;bde&quot;, &quot;bdf&quot;, &quot;cde&quot;, &quot;cdf&quot;].

Return all words that can be formed in this manner, in lexicographical order.

 

Example 1:
Input: &quot;{a,b}c{d,e}f&quot;
Output: [&quot;acdf&quot;,&quot;acef&quot;,&quot;bcdf&quot;,&quot;bcef&quot;]

Example 2:
Input: &quot;abcd&quot;
Output: [&quot;abcd&quot;]

 

Note:
	1 <= S.length <= 50
	There are no nested curly brackets.
	All characters inside a pair of consecutive opening and ending curly brackets are different.


"""
from typing import List
class Solution:
    def expand(self, S: str) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().expand(0) == 0

