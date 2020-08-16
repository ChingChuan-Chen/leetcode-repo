"""
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

 

Example 1:
Input: &quot;abbaca&quot;
Output: &quot;ca&quot;
Explanation: 
For example, in &quot;abbaca&quot; we could remove &quot;bb&quot; since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is &quot;aaca&quot;, of which only &quot;aa&quot; is possible, so the final string is &quot;ca&quot;.

 

Note:
	1 <= S.length <= 20000
	S consists only of English lowercase letters.

"""
class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().removeDuplicates(0) == 0

