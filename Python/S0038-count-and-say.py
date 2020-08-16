"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as &quot;one 1&quot; or 11.
11 is read off as &quot;two 1s&quot; or 21.
21 is read off as &quot;one 2, then one 1&quot; or 1211.

Given an integer n where 1 &le; n &le; 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:
Input: 1
Output: &quot;1&quot;
Explanation: This is the base case.

Example 2:
Input: 4
Output: &quot;1211&quot;
Explanation: For n = 3 the term was &quot;21&quot; in which we have two groups &quot;2&quot; and &quot;1&quot;, &quot;2&quot; can be read as &quot;12&quot; which means frequency = 1 and value = 2, the same way &quot;1&quot; is read as &quot;11&quot;, so the answer is the concatenation of &quot;12&quot; and &quot;11&quot; which is &quot;1211&quot;.


"""
class Solution:
    def countAndSay(self, n: int) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().countAndSay(0) == 0

