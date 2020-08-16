"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

	&quot;123&quot;
	&quot;132&quot;
	&quot;213&quot;
	&quot;231&quot;
	&quot;312&quot;
	&quot;321&quot;

Given n and k, return the kth permutation sequence.

Note:
	Given n will be between 1 and 9 inclusive.
	Given k will be between 1 and n! inclusive.

Example 1:
Input: n = 3, k = 3
Output: &quot;213&quot;

Example 2:
Input: n = 4, k = 9
Output: &quot;2314&quot;


"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().getPermutation(0) == 0

