"""
Given two strings S and T, each of which represents a non-negative rational number, return True if and only if they represent the same number. The strings may use parentheses to denote the repeating part of the rational number.

In general a rational number can be represented using up to three parts: an integer part, a non-repeating part, and a repeating part. The number will be represented in one of the following three ways:

	<IntegerPart> (e.g. 0, 12, 123)
	<IntegerPart><.><NonRepeatingPart>  (e.g. 0.5, 1., 2.12, 2.0001)
	<IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)> (e.g. 0.1(6), 0.9(9), 0.00(1212))

The repeating portion of a decimal expansion is conventionally denoted within a pair of round brackets.  For example:

1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)

Both 0.1(6) or 0.1666(6) or 0.166(66) are correct representations of 1 / 6.

 

Example 1:
Input: S = &quot;0.(52)&quot;, T = &quot;0.5(25)&quot;
Output: true
Explanation:
Because &quot;0.(52)&quot; represents 0.52525252..., and &quot;0.5(25)&quot; represents 0.52525252525..... , the strings represent the same number.

Example 2:
Input: S = &quot;0.1666(6)&quot;, T = &quot;0.166(66)&quot;
Output: true

Example 3:
Input: S = &quot;0.9(9)&quot;, T = &quot;1.&quot;
Output: true
Explanation: 
&quot;0.9(9)&quot; represents 0.999999999... repeated forever, which equals 1.  [See this link for an explanation.]
&quot;1.&quot; represents the number 1, which is formed correctly: (IntegerPart) = &quot;1&quot; and (NonRepeatingPart) = &quot;&quot;.

 

Note:
	Each part consists only of digits.
	The <IntegerPart> will not begin with 2 or more zeros.  (There is no other restriction on the digits of each part.)
	1 <= <IntegerPart>.length <= 4 
	0 <= <NonRepeatingPart>.length <= 4 
	1 <= <RepeatingPart>.length <= 4


"""
class Solution:
    def isRationalEqual(self, S: str, T: str) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().isRationalEqual(0) == 0

