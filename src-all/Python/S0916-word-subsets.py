"""
We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, &quot;wrr&quot; is a subset of &quot;warrior&quot;, but is not a subset of &quot;world&quot;.

Now say a word a from A is universal if for every b in B, b is a subset of a. 

Return a list of all universal words in A.  You can return the words in any order.

 

Example 1:
Input: A = [&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;], B = [&quot;e&quot;,&quot;o&quot;]
Output: [&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;]

Example 2:
Input: A = [&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;], B = [&quot;l&quot;,&quot;e&quot;]
Output: [&quot;apple&quot;,&quot;google&quot;,&quot;leetcode&quot;]

Example 3:
Input: A = [&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;], B = [&quot;e&quot;,&quot;oo&quot;]
Output: [&quot;facebook&quot;,&quot;google&quot;]

Example 4:
Input: A = [&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;], B = [&quot;lo&quot;,&quot;eo&quot;]
Output: [&quot;google&quot;,&quot;leetcode&quot;]

Example 5:
Input: A = [&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;], B = [&quot;ec&quot;,&quot;oc&quot;,&quot;ceo&quot;]
Output: [&quot;facebook&quot;,&quot;leetcode&quot;]

 

Note:
	1 <= A.length, B.length <= 10000
	1 <= A[i].length, B[i].length <= 10
	A[i] and B[i] consist only of lowercase letters.
	All words in A[i] are unique: there isn&#39;t i != j with A[i] == A[j].


"""
from typing import List
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().wordSubsets(0) == 0

