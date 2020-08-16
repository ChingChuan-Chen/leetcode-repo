"""
Given strings A and B of the same length, we say A[i] and B[i] are equivalent characters. For example, if A = "abc" and B = "cde", then we have &#39;a&#39; == &#39;c&#39;, &#39;b&#39; == &#39;d&#39;, &#39;c&#39; == &#39;e&#39;.

Equivalent characters follow the usual rules of any equivalence relation:

	Reflexivity: &#39;a&#39; == &#39;a&#39;
	Symmetry: &#39;a&#39; == &#39;b&#39; implies &#39;b&#39; == &#39;a&#39;
	Transitivity: &#39;a&#39; == &#39;b&#39; and &#39;b&#39; == &#39;c&#39; implies &#39;a&#39; == &#39;c&#39;

For example, given the equivalency information from A and B above, S = "eed", "acd", and "aab" are equivalent strings, and "aab" is the lexicographically smallest equivalent string of S.

Return the lexicographically smallest equivalent string of S by using the equivalency information from A and B.

 

Example 1:
Input: A = "parker", B = "morris", S = "parser"
Output: "makkek"
Explanation: Based on the equivalency information in A and B, we can group their characters as [m,p], [a,o], [k,r,s], [e,i]. The characters in each group are equivalent and sorted in lexicographical order. So the answer is "makkek".

Example 2:
Input: A = "hello", B = "world", S = "hold"
Output: "hdld"
Explanation:  Based on the equivalency information in A and B, we can group their characters as [h,w], [d,e,o], [l,r]. So only the second letter &#39;o&#39; in S is changed to &#39;d&#39;, the answer is "hdld".

Example 3:
Input: A = "leetcode", B = "programs", S = "sourcecode"
Output: "aauaaaaada"
Explanation:  We group the equivalent characters in A and B as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in S except &#39;u&#39; and &#39;d&#39; are transformed to &#39;a&#39;, the answer is "aauaaaaada".

 

Note:
	String A, B and S consist of only lowercase English letters from &#39;a&#39; - &#39;z&#39;.
	The lengths of string A, B and S are between 1 and 1000.
	String A and B are of the same length.

"""
class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().smallestEquivalentString(0) == 0

