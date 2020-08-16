"""
Let&#39;s say a positive integer is a superpalindrome if it is a palindrome, and it is also the square of a palindrome.

Now, given two positive integers L and R (represented as strings), return the number of superpalindromes in the inclusive range [L, R].

 

Example 1:
Input: L = &quot;4&quot;, R = &quot;1000&quot;
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.

 

Note:
	1 <= len(L) <= 18
	1 <= len(R) <= 18
	L and R are strings representing integers in the range [1, 10^18).
	int(L) <= int(R)

 


"""
class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().superpalindromesInRange(0) == 0

