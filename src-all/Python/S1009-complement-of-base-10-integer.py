"""
Every non-negative integer N has a binary representation.  For example, 5 can be represented as &quot;101&quot; in binary, 11 as &quot;1011&quot; in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of &quot;101&quot; in binary is &quot;010&quot; in binary.

For a given number N in base-10, return the complement of it&#39;s binary representation as a base-10 integer.

 

Example 1:
Input: 5
Output: 2
Explanation: 5 is &quot;101&quot; in binary, with complement &quot;010&quot; in binary, which is 2 in base-10.

Example 2:
Input: 7
Output: 0
Explanation: 7 is &quot;111&quot; in binary, with complement &quot;000&quot; in binary, which is 0 in base-10.

Example 3:
Input: 10
Output: 5
Explanation: 10 is &quot;1010&quot; in binary, with complement &quot;0101&quot; in binary, which is 5 in base-10.

 

Note:
	0 <= N < 10^9
	This question is the same as 476: https://leetcode.com/problems/number-complement/


"""
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().bitwiseComplement(0) == 0

