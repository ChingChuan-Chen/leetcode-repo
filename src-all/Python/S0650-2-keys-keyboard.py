"""
Initially on a notepad only one character &#39;A&#39; is present. You can perform two operations on this notepad for each step:

	Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
	Paste: You can paste the characters which are copied last time.

 

Given a number n. You have to get exactly n &#39;A&#39; on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n &#39;A&#39;.

Example 1:
Input: 3
Output: 3
Explanation:
Intitally, we have one character &#39;A&#39;.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get &#39;AA&#39;.
In step 3, we use Paste operation to get &#39;AAA&#39;.

 

Note:
	The n will be in the range [1, 1000].

 

"""
class Solution:
    def minSteps(self, n: int) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().minSteps(0) == 0

