"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output  in any order.

 
Example 1:
Input: S = &quot;a1b2&quot;
Output: [&quot;a1b2&quot;,&quot;a1B2&quot;,&quot;A1b2&quot;,&quot;A1B2&quot;]

Example 2:
Input: S = &quot;3z4&quot;
Output: [&quot;3z4&quot;,&quot;3Z4&quot;]

Example 3:
Input: S = &quot;12345&quot;
Output: [&quot;12345&quot;]

Example 4:
Input: S = &quot;0&quot;
Output: [&quot;0&quot;]

 
Constraints:
	S will be a string with length between 1 and 12.
	S will consist only of letters or digits.


"""
from typing import List
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().letterCasePermutation(0) == 0

