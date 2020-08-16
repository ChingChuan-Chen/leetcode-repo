"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:
Input: &quot;A&quot;
Output: 1

Example 2:
Input: &quot;AB&quot;
Output: 28

Example 3:
Input: &quot;ZY&quot;
Output: 701

 
Constraints:
	1 <= s.length <= 7
	s consists only of uppercase English letters.
	s is between &quot;A&quot; and &quot;FXSHRXW&quot;.


"""
class Solution:
    def titleToNumber(self, s: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().titleToNumber(0) == 0

