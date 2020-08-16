"""
We are given S, a length n string of characters from the set {&#39;D&#39;, &#39;I&#39;}. (These letters stand for &quot;decreasing&quot; and &quot;increasing&quot;.)

A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1, ..., n}, such that for all i:

	If S[i] == &#39;D&#39;, then P[i] > P[i+1], and;
	If S[i] == &#39;I&#39;, then P[i] < P[i+1].

How many valid permutations are there?  Since the answer may be large, return your answer modulo 10^9 + 7.

 

Example 1:
Input: &quot;DID&quot;
Output: 5
Explanation: 
The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)

 

Note:
	1 <= S.length <= 200
	S consists only of characters from the set {&#39;D&#39;, &#39;I&#39;}.

 


"""
class Solution:
    def numPermsDISequence(self, S: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().numPermsDISequence(0) == 0

