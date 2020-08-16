"""
Sometimes people repeat letters to represent extra feeling, such as &quot;hello&quot; -> &quot;heeellooo&quot;, &quot;hi&quot; -> &quot;hiiii&quot;.  In these strings like &quot;heeellooo&quot;, we have groups of adjacent letters that are all the same:  &quot;h&quot;, &quot;eee&quot;, &quot;ll&quot;, &quot;ooo&quot;.

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with &quot;hello&quot;, we could do an extension on the group &quot;o&quot; to get &quot;hellooo&quot;, but we cannot get &quot;helloo&quot; since the group &quot;oo&quot; has size less than 3.  Also, we could do another extension like &quot;ll&quot; -> &quot;lllll&quot; to get &quot;helllllooo&quot;.  If S = &quot;helllllooo&quot;, then the query word &quot;hello&quot; would be stretchy because of these two extension operations: query = &quot;hello&quot; -> &quot;hellooo&quot; -> &quot;helllllooo&quot; = S.

Given a list of query words, return the number of words that are stretchy. 

 

Example:
Input: 
S = &quot;heeellooo&quot;
words = [&quot;hello&quot;, &quot;hi&quot;, &quot;helo&quot;]
Output: 1
Explanation: 
We can extend &quot;e&quot; and &quot;o&quot; in the word &quot;hello&quot; to get &quot;heeellooo&quot;.
We can&#39;t extend &quot;helo&quot; to get &quot;heeellooo&quot; because the group &quot;ll&quot; is not size 3 or more.

 
Constraints:
	0 <= len(S) <= 100.
	0 <= len(words) <= 100.
	0 <= len(words[i]) <= 100.
	S and all words in words consist only of lowercase letters


"""
from typing import List
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().expressiveWords(0) == 0

